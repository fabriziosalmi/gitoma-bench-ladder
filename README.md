# Rung 3 — Python + SQLite: SQL injection in `find_user_by_name`

## What this rung tests

Semantic security bug. The file compiles fine (no Build Integrity fail), but a single function leaks the entire users table to anyone who supplies a malicious name. This is the canonical SQL-injection pattern; gitoma's devil should flag it as a `¬S` (anti-hope) blocker and the worker should reach for the parameterised-query idiom.

## The injected bug

`src/db.py:53` — `f"SELECT id, name FROM users WHERE name = '{name}'"`. 
F-string interpolation lets the caller close the SQL literal and inject arbitrary statements. The two adversarial tests in `tests/test_db.py` make this concrete:

- `test_no_sql_injection`: name = `"' OR '1'='1"` — bypasses WHERE, returns all 3 users pre-fix.
- `test_no_sql_injection_via_comment`: name = `"alice'; --"` — truncates the query via SQL line comment.

## The fix

```python
cur = conn.execute(
    "SELECT id, name FROM users WHERE name = ?",
    (name),
)
```

Stdlib `sqlite3` binds the parameter — the input is never parsed as SQL. This is the canonical fix; any equivalent (named binding, prepared statement) is fine as long as the f-string is removed.

The other functions in `src/db.py` (`get_conn`, `init_schema`, `seed`) are correct. If gitoma touches them, that's a regression.

## Running locally

```bash
cd rung-3
python -m pytest -q
```

Expected (pre-fix): 2 fail (the two injection tests), 2 pass.
Expected (post-fix): 4 pass.

## Running gitoma on this rung

From minimac:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

Scoring:

```python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Installation

This project is a benchmark suite for testing security vulnerabilities in Python code, specifically focusing on SQL injection patterns using SQLite.

**Prerequisites:**
- Python 3.x
- `pytest`

**Installation:**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd gitoma-bench-ladder
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # Assuming a requirements file exists, or adjust as necessary
   # Or install directly:
   pip install pytest
   ```

## Usage

This repository is designed to be run by the `gitoma` tool to benchmark code changes against known vulnerability patterns.

**To run tests locally:**
```bash
python -m pytest -q
```

**To run gitoma against this rung:**
Use the following command to execute the benchmark on a specific rung:
```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

## Contributing

Contributions are welcome! If you find a bug or have an idea for improvement, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Ensure your changes pass all existing tests and adhere to the project's coding standards.

## Example

This example demonstrates how to run the benchmark for Rung 3:

```bash
# Run locally to see expected failures/passes
python -m pytest -q

# Run gitoma against this rung (replace <PR-URL> with the actual PR URL)
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```