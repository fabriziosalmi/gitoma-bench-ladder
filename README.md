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

This project is a benchmark for security vulnerabilities in Python code, specifically focusing on SQL injection patterns. 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
   cd gitoma-bench-ladder
   ```

2. **Install dependencies:**
   This project requires Python 3 and `pytest`.
   ```bash
   pip install -r requirements.txt  # Assuming a requirements file exists, adjust as necessary
   # Or install directly:
   pip install pytest
   ```

## Usage

### Local Testing

To run the tests locally against this specific rung:

```bash
cd rung-3
python -m pytest -q
```

### Running with gitoma

To run the security analysis tool on a specific rung:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

To score a specific rung against a Pull Request:

```python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Contributing

Contributions are welcome! If you find bugs, security issues, or improvements to the testing harness, please open an issue or submit a Pull Request.

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please ensure your changes pass all existing tests before submitting.

## Example

This rung demonstrates a critical vulnerability where string formatting is used directly in an SQL query, leading to SQL injection.

**Vulnerable Code Snippet (in `src/db.py`):**
```python
# Vulnerable line:
SELECT id, name FROM users WHERE name = '{name}'
```

**The Fix (using parameter binding):**
```python
cur = conn.execute(
    "SELECT id, name FROM users WHERE name = ?",
    (name),
)
```

This example illustrates the principle: always use parameterised queries when constructing SQL statements with external input.
