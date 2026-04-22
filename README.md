# gitoma-bench-ladder

Deterministic benchmark ladder for gitoma. 8 rungs of increasing
complexity, each testing ONE new axis of difficulty so failures are
diagnosable.

## Layout

- `main` branch: bench harness + this README. No rung code here.
- `rung-N` (orphan branches): each contains the code-under-test for
  that rung at the root. Gitoma runs against them via `--base rung-N`.
- `bench/bench_rung.py`: score harness. Reads `golden.json` + the PR
  gitoma produced, emits JSON scorecard.

## The rungs

| # | Language | Tests |
|---|----------|-------|
| 0 | Python   | single file, one bug |
| 1 | Go       | two files, cross-file dep |
| 2 | Rust     | tiny HTTP API (axum) |
| 3 | Python   | API + SQLite (SQLAlchemy) |
| 4 | JS       | API + DB + frontend (XSS/CSRF bait) |
| 5 | Go       | + auth (JWT, IDOR bait) |
| 6 | Rust     | + concurrency (locks, Send/Sync) |
| 7 | Go       | + race conditions (goroutines, `go test -race`) |

## Running a rung

From minimac (the host with gitoma installed):

```
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-0 --reset -y
```

Then from this repo locally:

```
python bench/bench_rung.py --rung 0 --pr-url <url-printed-by-gitoma>
```

## Score schema

Each run emits a JSON scorecard with these columns:

- `patch_coverage`: expected_files_touched ∩ actual / expected
- `test_health`: pytest / cargo test / go test / npm test verdict after PR applied
- `loc_added`, `loc_modified`: unified-diff measurements
- `omega` (Ψ-lite Ω): `loc_added / max(loc_modified, 1)` — bloat factor
- `gamma_pre`, `gamma_post` (Ψ-lite Γ): linter violation counts before/after
  (ruff / clippy / golangci-lint / eslint depending on rung)

Γ and Ω are logged as **measurements only** — not gates. When we have
3+ rungs of data across 2+ models and Γ/Ω predict test_health with
r² ≥ 0.4, we promote them to acceptance criteria.
