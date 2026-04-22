# Rung 3 — Python + SQLite: SQL injection in `find_user_by_name`

## What this rung tests

Semantic security bug. The file compiles fine (no Build Integrity fail), but a single function leaks the entire users table to anyone who supplies a malicious name. This is the canonical SQL-injection pattern; gitoma's devil should flag it as a `¬S` (anti-hope) blocker and the worker should reach for the parameterised-query idiom.

## The injected bug

`src/db.py:53` — `f"SELECT id, name FROM users WHERE name = '{name}'"`. F-string interpolation lets the caller close the SQL literal and inject arbitrary statements. The two adversarial tests in `tests/test_db.py` make this concrete:

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

```bash
python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Installation

To run this rung locally, ensure you have Python installed.

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd rung-3
   ```
2. Install dependencies (assuming a requirements file exists or using pip):
   ```bash
   pip install -r requirements.txt  # Or install necessary packages
   ```

## Usage

This rung is designed to test security vulnerabilities, specifically SQL injection. Use the provided commands to run local tests or integrate with gitoma.

*   **Local Testing:** Run unit tests to verify the fix:
    ```bash
    python -m pytest -q
    ```
*   **Gitoma Benchmarking:** Run the benchmark against a specific PR:
    ```bash
    python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
    ```

## Contributing

Contributions are welcome! If you find other security issues or improvements, please open an issue or submit a Pull Request.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Test your changes with unit tests and ensure no regressions are introduced.
5.  Commit your changes (`git commit -m 'feat: Describe your changes'`).
6.  Push to the branch and open a Pull Request.

## License

This project is licensed under the MIT License - see the 
LICENSE file for details.
