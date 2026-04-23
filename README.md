# Rung 3 — Python + SQLite: SQL injection in `find_user_by_name`

## Overview

This rung tests a semantic security vulnerability in the `find_user_by_name` function within `src/db.py`. The vulnerability is an SQL injection flaw caused by using f-string interpolation to construct a SQL query, which allows an attacker to manipulate the query logic.

**Goal:** To ensure that database interactions use parameterised queries to prevent SQL injection.

## The Injected Bug

The vulnerable code snippet is located at `src/db.py:53`:

```python
# Vulnerable code example (in src/db.py):
# f"SELECT id, name FROM users WHERE name = '{name}'"
```

This allows arbitrary SQL to be executed if the `name` parameter is supplied maliciously.

## The Fix

The fix involves replacing the f-string interpolation with a parameterised query using the `sqlite3` library's binding mechanism:

```python
cur = conn.execute(
    "SELECT id, name FROM users WHERE name = ?",
    (name,),
)
```

This ensures that user input is treated strictly as data, not executable SQL.

## Testing and Verification

### Local Testing

To test the vulnerability, run pytest:

```bash
cd rung-3
python -m pytest -q
```

*   **Expected (pre-fix):** 2 failures (the two injection tests), 2 passes.
*   **Expected (post-fix):** 4 passes.

### Running with gitoma

To run this rung through the full bench suite:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder 
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

### Scoring Reference

Scoring for this rung can be retrieved via:

```bash
python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Code Structure Notes

*   The fix is applied in `src/db.py` by using parameter binding.
*   Other functions in `src/db.py` (`get_conn`, `init_schema`, `seed`) are assumed to be correct and must not be modified.
