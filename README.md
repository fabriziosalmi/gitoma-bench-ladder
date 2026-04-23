# Rung 3 — Python + SQLite: SQL injection in `find_user_by_name`

## What this rung tests

Semantic security bug. The file compiles fine (no Build Integrity fail), but a single function leaks the entire users table to anyone who supplies a malicious name. This is the canonical SQL-injection
pattern; gitoma's devil should flag it as a `¬S` (anti-hope) blocker
and the worker should reach for the parameterised-query idiom.

## The injected bug

`src/db.py:53` — `f"SELECT id, name FROM users WHERE name = '{name}'"`. 
F-string interpolation lets the caller close the SQL literal and
inject arbitrary statements. The two adversarial tests in
`tests/test_db.py` make this concrete:

- `test_no_sql_injection`: name = `"' OR '1'='1"` — bypasses WHERE,
  returns all 3 users pre-fix.
- `test_no_sql_injection_via_comment`: name = `"alice'; --"` —
  truncates the query via SQL line comment.

## The fix

```python
cur = conn.execute(
    "SELECT id, name FROM users WHERE name = ?",
    (name),
)
```

Stdlib `sqlite3` binds the parameter — the input is never parsed
as SQL. This is the canonical fix; any equivalent (named binding, prepared statement)
is fine as long as the f-string is removed.

The other functions in `src/db.py` (`get_conn`, `init_schema`, `seed`)
are correct. If gitoma touches them, that's a regression.

## Usage

This rung tests the security vulnerability in `find_user_by_name` by attempting to inject SQL.

### Running locally (for testing the fix)

To run the unit tests for this rung locally:
```bash
cd rung-3
python -m pytest -q
```

### Running gitoma on this rung

To run the security analysis tool `gitoma` against this specific rung:
```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder 
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

## Example

This section demonstrates how to run the security analysis using `gitoma`.

1. Ensure you are in the root directory of the repository.
2. Execute the command below to run `gitoma` against rung 3:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder 
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

Scoring:

```python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Installation

### Prerequisites

* Python 3.x
* Gitoma installed (or available via pip/local setup)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
   cd gitoma-bench-ladder
   ```

2. Install dependencies:
   This project relies on Python packages defined in `pyproject.toml`.
   ```bash
   pip install -r requirements.txt  # Assuming a requirements file exists, or adjust as necessary
   # If using pyproject.toml for installation:
   # pip install -e .
   ```

3. Run tests (for local verification):
   ```bash
   cd rung-3
   python -m pytest -q
   ```

### Running Benchmarks

To run the specific rung tests locally:

```bash
cd rung-3
python -m pytest -q
```

To run gitoma against this rung:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder 
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```