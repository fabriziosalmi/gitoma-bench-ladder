# Rung 0 — single file, single bug

## What this rung tests

The most basic worker-fix-testpass loop: gitoma reads one broken
Python file, spots the bug, proposes a one-line fix, pytest passes.

**No panel complexity, no cross-file reasoning, no dependency graph.**

If this rung does not pass, nothing above it will — full stop.

## The injected bug

`calc.py:18` — `average()` divides by `len(nums) - 1` instead of
`len(nums)`. Classic off-by-one.

The failing test `test_average_of_three` pins the bug.

## Running the test locally

```
cd rung-0
python -m pytest -q
```

Expected (pre-fix): 2 fail, 1 pass. The buggy line breaks both
`test_average_of_three` (wrong result) and `test_average_single`
(ZeroDivisionError). `test_average_empty_raises` passes because the
early-return runs before the buggy arithmetic.

Expected (post-fix): 3 pass.

## Running gitoma on this rung

From minimac:

```
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-0 --reset -y
```

Gitoma will create a working branch off `rung-0`, fix the bug, open
a PR targeting `rung-0`.

## Running gitoma on this rung (Installation)

To run tests or use the toolchain, install the required dependencies:

```bash
pip install -r requirements-test.txt
```

## Scoring

From this repo's `main` branch:

```python
bench/bench_rung.py --rung 0 --pr-url <url-printed-by-gitoma>
```