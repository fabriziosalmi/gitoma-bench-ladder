#!/usr/bin/env python3
"""Score a gitoma PR against a rung's golden fixture.

Usage:
    bench_rung.py --rung N --pr-url https://github.com/.../pull/NN

Reads:
  - ``rung-N/golden.json`` from the matching orphan branch (fetched via ``gh``)
  - The PR diff (via ``gh pr diff``)

Writes:
  - stdout: human-readable table
  - bench/results/rung-N-<timestamp>.json: machine-readable scorecard

Columns (V0):
  patch_coverage  test_health  loc_added  loc_modified  omega  gamma_pre  gamma_post

Ψ-lite note: gamma_pre/gamma_post are raw linter-violation counts.
We do NOT compute a scalar Ψ until we have multi-rung / multi-model
data to justify α/λ weights. See README.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

REPO_DEFAULT = "fabriziosalmi/gitoma-bench-ladder"


def _run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=check)


def _extract_pr_number(pr_url: str) -> int:
    m = re.search(r"/pull/(\d+)", pr_url)
    if not m:
        raise ValueError(f"cannot parse PR number from {pr_url!r}")
    return int(m.group(1))


def _fetch_diff(repo: str, pr_number: int) -> str:
    return _run(["gh", "pr", "diff", str(pr_number), "--repo", repo]).stdout


def _diff_loc_and_files(diff: str) -> tuple[int, int, set[str]]:
    added = 0
    removed = 0
    touched: set[str] = set()
    for line in diff.splitlines():
        m = re.match(r"^diff --git a/(\S+) b/\S+", line)
        if m:
            touched.add(m.group(1))
            continue
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+"):
            added += 1
        elif line.startswith("-"):
            removed += 1
    return added, removed, touched


def _fetch_golden(repo: str, rung: int, ref: str) -> dict:
    """Fetch ``golden.json`` from the rung's branch via gh API (avoids a clone)."""
    api = f"/repos/{repo}/contents/golden.json?ref={ref}"
    raw = _run(["gh", "api", "-H", "Accept: application/vnd.github.raw", api]).stdout
    return json.loads(raw)


def _apply_pr_and_run_tests(repo: str, pr_number: int, base: str, rung: int) -> tuple[str, dict[str, object]]:
    """Clone the base branch, fetch+apply the PR head as a merge, run tests.

    Returns (verdict, detail_dict).
    verdict ∈ {"pass", "fail", "error", "no_tests"}.
    """
    workdir = Path(tempfile.mkdtemp(prefix=f"bench-rung-{rung}-"))
    clone_url = f"https://github.com/{repo}.git"
    _run(["git", "clone", "--branch", base, "--depth=1", clone_url, str(workdir)])

    # Fetch the PR head and merge into base (pure worktree — no push)
    _run(["git", "fetch", "origin", f"pull/{pr_number}/head:pr-{pr_number}"], cwd=workdir)
    merge = _run(["git", "merge", "--no-edit", f"pr-{pr_number}"], cwd=workdir, check=False)
    if merge.returncode != 0:
        return "error", {"merge_conflict": True, "stderr": merge.stderr[-500:]}

    # Detect test framework. Order matters: language markers (Cargo.toml,
    # go.mod, package.json) win over the generic ``tests/`` dir, because a
    # Rust crate has ``tests/`` for integration tests too — picking pytest
    # there silently runs zero tests and reports failure (caught live on
    # rung-2 where a clean Rust PR was scored as failing pytest).
    has_cargo = (workdir / "Cargo.toml").exists()
    has_gomod = (workdir / "go.mod").exists()
    has_npm = (workdir / "package.json").exists()
    has_pytest = (
        not (has_cargo or has_gomod or has_npm)
        and (
            (workdir / "pyproject.toml").exists()
            or (workdir / "setup.py").exists()
            or any(p.name.startswith("test_") and p.suffix == ".py" for p in workdir.iterdir() if p.is_file())
            or any(p.suffix == ".py" for p in workdir.iterdir() if p.is_file())
        )
    )

    if has_cargo:
        r = _run(["cargo", "test", "--quiet"], cwd=workdir, check=False)
        return ("pass" if r.returncode == 0 else "fail"), {"framework": "cargo", "exit": r.returncode, "tail": r.stdout[-500:] + r.stderr[-500:]}
    if has_gomod:
        r = _run(["go", "test", "./..."], cwd=workdir, check=False)
        return ("pass" if r.returncode == 0 else "fail"), {"framework": "go", "exit": r.returncode, "tail": r.stdout[-500:] + r.stderr[-500:]}
    if has_npm:
        r = _run(["npm", "test", "--silent"], cwd=workdir, check=False)
        return ("pass" if r.returncode == 0 else "fail"), {"framework": "npm", "exit": r.returncode, "tail": r.stdout[-500:] + r.stderr[-500:]}
    if has_pytest:
        r = _run(["python", "-m", "pytest", "-q", "--no-header"], cwd=workdir, check=False)
        verdict = "pass" if r.returncode == 0 else "fail"
        detail = {"framework": "pytest", "exit": r.returncode, "tail": r.stdout[-500:] + r.stderr[-500:]}
        return verdict, detail

    return "no_tests", {"reason": "no test framework markers found at repo root"}


def _ruff_count(path: Path) -> int:
    """Return count of ruff violations under path, or -1 on error."""
    r = _run(["ruff", "check", str(path), "--output-format=json"], check=False)
    if r.returncode not in (0, 1):
        return -1
    try:
        return len(json.loads(r.stdout or "[]"))
    except json.JSONDecodeError:
        return -1


@dataclass
class Scorecard:
    rung: int
    pr_url: str
    pr_number: int
    base_branch: str
    touched_files: list[str]
    expected_files: list[str]
    patch_coverage: float
    test_health: str
    test_detail: dict
    loc_added: int
    loc_modified: int
    omega: float
    gamma_pre: int
    gamma_post: int
    ts: str


def score(rung: int, pr_url: str, repo: str = REPO_DEFAULT) -> Scorecard:
    pr_number = _extract_pr_number(pr_url)
    base = f"rung-{rung}"

    # Fetch PR metadata (to learn the head SHA for gamma_post linting)
    diff = _fetch_diff(repo, pr_number)
    added, removed, touched = _diff_loc_and_files(diff)
    omega = added / max(removed, 1)

    golden = _fetch_golden(repo, rung, base)
    expected = set(golden.get("expected_patches_must_touch", []))
    coverage = len(expected & touched) / max(len(expected), 1)

    # Test health: clone + merge PR + run tests
    verdict, detail = _apply_pr_and_run_tests(repo, pr_number, base, rung)

    # Γ pre/post: lint the base branch, then lint the merged worktree
    gamma_pre = gamma_post = -1
    if detail.get("framework") == "pytest" or golden.get("language") == "python":
        # Clone base again (fresh) for pre-state
        with tempfile.TemporaryDirectory() as pre_tmp:
            _run(["git", "clone", "--branch", base, "--depth=1", f"https://github.com/{repo}.git", pre_tmp])
            gamma_pre = _ruff_count(Path(pre_tmp))
        # Gamma post: the workdir from _apply_pr_and_run_tests is already gone
        # (tempfile cleanup happened). For V0 we re-apply briefly.
        with tempfile.TemporaryDirectory() as post_tmp:
            _run(["git", "clone", "--branch", base, "--depth=1", f"https://github.com/{repo}.git", post_tmp])
            _run(["git", "fetch", "origin", f"pull/{pr_number}/head:pr-{pr_number}"], cwd=Path(post_tmp))
            _run(["git", "merge", "--no-edit", f"pr-{pr_number}"], cwd=Path(post_tmp), check=False)
            gamma_post = _ruff_count(Path(post_tmp))

    return Scorecard(
        rung=rung,
        pr_url=pr_url,
        pr_number=pr_number,
        base_branch=base,
        touched_files=sorted(touched),
        expected_files=sorted(expected),
        patch_coverage=round(coverage, 3),
        test_health=verdict,
        test_detail=detail,
        loc_added=added,
        loc_modified=removed,
        omega=round(omega, 3),
        gamma_pre=gamma_pre,
        gamma_post=gamma_post,
        ts=dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
    )


def _print_table(s: Scorecard) -> None:
    print()
    print(f"=== RUNG {s.rung} SCORECARD (PR #{s.pr_number}) ===")
    print(f"  ts            : {s.ts}")
    print(f"  base_branch   : {s.base_branch}")
    print(f"  pr_url        : {s.pr_url}")
    print()
    print(f"  patch_coverage: {s.patch_coverage:.2f}   (expected: {s.expected_files})")
    print(f"  touched_files : {s.touched_files}")
    print(f"  test_health   : {s.test_health}   ({s.test_detail.get('framework', '?')})")
    print()
    print(f"  loc_added     : {s.loc_added}")
    print(f"  loc_modified  : {s.loc_modified}")
    print(f"  omega (Ψ-lite): {s.omega:.2f}     (lower = less bloat)")
    print()
    print(f"  gamma_pre     : {s.gamma_pre}")
    print(f"  gamma_post    : {s.gamma_post}")
    if s.gamma_pre >= 0 and s.gamma_post >= 0:
        ratio = (s.gamma_pre + 1) / (s.gamma_post + 1)
        print(f"  gamma_ratio   : {ratio:.2f}     (>1 = fewer lint issues after)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rung", type=int, required=True)
    ap.add_argument("--pr-url", required=True)
    ap.add_argument("--repo", default=REPO_DEFAULT)
    args = ap.parse_args()

    s = score(args.rung, args.pr_url, args.repo)
    _print_table(s)

    out_dir = Path(__file__).parent / "results"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"rung-{args.rung}-{dt.datetime.now(dt.UTC).strftime('%Y%m%dT%H%M%S')}.json"
    out_path.write_text(json.dumps(asdict(s), indent=2))
    print(f"\n  → written: {out_path}")
    return 0 if s.test_health == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
