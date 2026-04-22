#!/usr/bin/env python3
"""Build a static HTML page from bench/results/*.json scorecards.

Pure stdlib. Run as ``python bench/build_site.py docs/`` (defaults to
``docs/`` in the repo root). The output is one ``index.html`` with the
full bench table + a per-rung summary, plus ``bench.json`` for anyone
who wants to slice the raw data.

Design choices:
  * Single self-contained HTML file, no external CSS / JS deps.
  * Tiny vanilla-JS sort on click — no jQuery, no React.
  * Colour-coded ``test_health`` (green/red) and ``omega`` (green<5,
    amber<15, red≥15) so a glance tells you "this row is healthy" or
    "this row is bloated".
  * Per-rung summary above the table: rows, pass-rate, mean Ω,
    median Ω. Without aggregation a 50-row table is noise.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import statistics
import sys
from pathlib import Path


_ROOT = Path(__file__).resolve().parents[1]
_RESULTS = _ROOT / "bench" / "results"


def load_scorecards(results_dir: Path) -> list[dict]:
    cards: list[dict] = []
    for p in sorted(results_dir.glob("rung-*.json")):
        try:
            cards.append(json.loads(p.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError):
            continue
    # Sort newest first within each rung; rung asc, ts desc
    cards.sort(key=lambda c: (c.get("rung", -1), c.get("ts", "")))
    return cards


def _omega_class(om: float | None) -> str:
    if om is None:
        return ""
    if om < 5:
        return "good"
    if om < 15:
        return "warn"
    return "bad"


def _gamma_cell(g: int | None) -> str:
    if g is None or g < 0:
        return "—"
    return str(g)


def _per_rung_summary(cards: list[dict]) -> list[dict]:
    by_rung: dict[int, list[dict]] = {}
    for c in cards:
        by_rung.setdefault(c.get("rung", -1), []).append(c)
    rows: list[dict] = []
    for rung in sorted(by_rung):
        rs = by_rung[rung]
        omegas = [c["omega"] for c in rs if c.get("omega") is not None]
        passes = sum(1 for c in rs if c.get("test_health") == "pass")
        cov = [c["patch_coverage"] for c in rs if c.get("patch_coverage") is not None]
        rows.append({
            "rung": rung,
            "samples": len(rs),
            "pass_rate": (passes / len(rs)) if rs else 0,
            "mean_omega": round(statistics.mean(omegas), 2) if omegas else None,
            "median_omega": round(statistics.median(omegas), 2) if omegas else None,
            "mean_coverage": round(statistics.mean(cov), 2) if cov else None,
        })
    return rows


_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>gitoma bench ladder — public scorecards</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root {{
  --fg: #e6e6e6;
  --bg: #0e1116;
  --bg2: #161b22;
  --muted: #8b949e;
  --good: #3fb950;
  --warn: #d29922;
  --bad: #f85149;
  --link: #58a6ff;
  --border: #30363d;
}}
* {{ box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  background: var(--bg);
  color: var(--fg);
  margin: 0;
  padding: 24px;
  font-size: 14px;
  line-height: 1.5;
}}
h1, h2 {{ font-weight: 600; }}
h1 {{ margin: 0 0 4px; font-size: 22px; }}
h2 {{ margin: 32px 0 12px; font-size: 16px; color: var(--muted); }}
.lead {{ color: var(--muted); margin: 0 0 24px; max-width: 880px; }}
.lead a {{ color: var(--link); text-decoration: none; }}
.lead a:hover {{ text-decoration: underline; }}
.meta {{ color: var(--muted); font-size: 12px; margin-bottom: 16px; }}
table {{
  border-collapse: collapse;
  width: 100%;
  background: var(--bg2);
  border: 1px solid var(--border);
  font-variant-numeric: tabular-nums;
}}
th, td {{
  padding: 8px 10px;
  text-align: left;
  border-bottom: 1px solid var(--border);
}}
th {{
  background: #1c2128;
  font-weight: 600;
  cursor: pointer;
  user-select: none;
  position: sticky;
  top: 0;
}}
th:hover {{ background: #22272e; }}
th:after {{ content: " ↕"; color: var(--muted); font-size: 11px; }}
tr:hover td {{ background: #1f242b; }}
td.num {{ text-align: right; }}
td a {{ color: var(--link); text-decoration: none; }}
td a:hover {{ text-decoration: underline; }}
.pill {{
  display: inline-block;
  padding: 1px 8px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 600;
}}
.th-pass    {{ background: rgba(63,185,80,0.15); color: var(--good); }}
.th-fail    {{ background: rgba(248,81,73,0.15); color: var(--bad); }}
.th-error   {{ background: rgba(210,153,34,0.15); color: var(--warn); }}
.th-no_tests {{ background: rgba(139,148,158,0.15); color: var(--muted); }}
.om-good    {{ color: var(--good); font-weight: 600; }}
.om-warn    {{ color: var(--warn); font-weight: 600; }}
.om-bad     {{ color: var(--bad); font-weight: 600; }}
.summary-table td:first-child {{ font-weight: 600; }}
footer {{ margin-top: 32px; color: var(--muted); font-size: 12px; }}
footer a {{ color: var(--link); text-decoration: none; }}
code {{ background: #1c2128; padding: 1px 6px; border-radius: 4px; }}
</style>
</head>
<body>

<h1>gitoma bench ladder</h1>
<p class="lead">
  Deterministic benchmark for <a href="https://github.com/fabriziosalmi/gitoma">gitoma</a>.
  Each row is one PR opened by the agent against a rung's golden fixture,
  scored deterministically by <code>bench/bench_rung.py</code>. Results are
  committed to the <code>main</code> branch — no after-the-fact editing,
  no cherry-picking. The numbers below are what the agent actually produced.
</p>

<p class="meta">{n_cards} scorecards · last build {built_at} UTC · source <a href="https://github.com/fabriziosalmi/gitoma-bench-ladder">github.com/fabriziosalmi/gitoma-bench-ladder</a></p>

<h2>Per-rung summary</h2>
<table class="summary-table">
<thead><tr>
  <th>rung</th><th>samples</th><th>pass rate</th>
  <th>mean Ω</th><th>median Ω</th><th>mean patch coverage</th>
</tr></thead>
<tbody>
{summary_rows}
</tbody>
</table>

<h2>All scorecards (click any header to sort)</h2>
<table id="bench">
<thead><tr>
  <th data-k="rung" data-num="1">rung</th>
  <th data-k="ts">date (UTC)</th>
  <th data-k="pr_number" data-num="1">PR</th>
  <th data-k="patch_coverage" data-num="1">patch cov</th>
  <th data-k="test_health">test</th>
  <th data-k="loc_added" data-num="1">+LOC</th>
  <th data-k="loc_modified" data-num="1">−LOC</th>
  <th data-k="omega" data-num="1">Ω<sub>Ψ-lite</sub></th>
  <th data-k="gamma_pre" data-num="1">Γ pre</th>
  <th data-k="gamma_post" data-num="1">Γ post</th>
</tr></thead>
<tbody>
{rows}
</tbody>
</table>

<footer>
  Ω = LOC added / max(LOC modified, 1) — bloat factor. Lower is tighter.<br>
  Γ = linter violations (raw count) — −1 when the language has no linter
  configured for the bench. Both are <em>measurement only</em>; not gates yet.<br>
  Raw machine-readable data: <a href="bench.json">bench.json</a>.
</footer>

<script>
(function() {{
  const t = document.getElementById('bench');
  if (!t) return;
  const tbody = t.querySelector('tbody');
  const headers = t.querySelectorAll('th');
  let sortDir = {{}};
  headers.forEach((th, i) => {{
    th.addEventListener('click', () => {{
      const numeric = th.dataset.num === '1';
      sortDir[i] = sortDir[i] === 1 ? -1 : 1;
      const dir = sortDir[i];
      const rows = Array.from(tbody.querySelectorAll('tr'));
      rows.sort((a, b) => {{
        const ax = a.cells[i].dataset.s ?? a.cells[i].textContent.trim();
        const bx = b.cells[i].dataset.s ?? b.cells[i].textContent.trim();
        if (numeric) return dir * (parseFloat(ax) - parseFloat(bx));
        return dir * ax.localeCompare(bx);
      }});
      rows.forEach(r => tbody.appendChild(r));
    }});
  }});
}})();
</script>
</body>
</html>
"""


def render_html(cards: list[dict]) -> str:
    summary = _per_rung_summary(cards)
    summary_rows = "\n".join(
        f"<tr>"
        f"<td>{s['rung']}</td>"
        f"<td class='num'>{s['samples']}</td>"
        f"<td class='num'>{s['pass_rate']*100:.0f}%</td>"
        f"<td class='num'>{s['mean_omega'] if s['mean_omega'] is not None else '—'}</td>"
        f"<td class='num'>{s['median_omega'] if s['median_omega'] is not None else '—'}</td>"
        f"<td class='num'>{s['mean_coverage'] if s['mean_coverage'] is not None else '—'}</td>"
        f"</tr>"
        for s in summary
    )

    rows = []
    for c in cards:
        om = c.get("omega")
        omega_disp = f"{om:.2f}" if isinstance(om, (int, float)) else "—"
        rows.append(
            "<tr>"
            f"<td>{c.get('rung','')}</td>"
            f"<td data-s='{c.get('ts','')}'>{c.get('ts','')[:16].replace('T',' ')}</td>"
            f"<td class='num'><a href='{c.get('pr_url','')}'>#{c.get('pr_number','?')}</a></td>"
            f"<td class='num'>{c.get('patch_coverage','—')}</td>"
            f"<td><span class='pill th-{c.get('test_health','?')}'>{c.get('test_health','?')}</span></td>"
            f"<td class='num'>{c.get('loc_added','—')}</td>"
            f"<td class='num'>{c.get('loc_modified','—')}</td>"
            f"<td class='num om-{_omega_class(om)}'>{omega_disp}</td>"
            f"<td class='num'>{_gamma_cell(c.get('gamma_pre'))}</td>"
            f"<td class='num'>{_gamma_cell(c.get('gamma_post'))}</td>"
            "</tr>"
        )

    return _HTML.format(
        n_cards=len(cards),
        built_at=_dt.datetime.now(_dt.UTC).strftime("%Y-%m-%d %H:%M"),
        summary_rows=summary_rows,
        rows="\n".join(rows),
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "out_dir",
        nargs="?",
        default="docs",
        help="Where to write the static site (default: ./docs)",
    )
    args = ap.parse_args()

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(exist_ok=True, parents=True)

    cards = load_scorecards(_RESULTS)
    if not cards:
        print(f"WARN: no scorecards found under {_RESULTS}", file=sys.stderr)

    (out_dir / "index.html").write_text(render_html(cards), encoding="utf-8")
    (out_dir / "bench.json").write_text(
        json.dumps(cards, indent=2, sort_keys=True), encoding="utf-8"
    )

    print(f"Wrote {out_dir / 'index.html'} + bench.json with {len(cards)} scorecard(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
