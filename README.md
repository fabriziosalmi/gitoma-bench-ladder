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

```bash
python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Installation

### Prerequisites

Ensure you have Python 3.x and `pytest` installed.

```bash
pip install pytest
```

### Setup

Clone the repository and navigate to the rung directory:

```bash
git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
cd rung-3
```

## Usage Examples

### Running Tests

To run the unit tests for this rung:

```bash
python -m pytest
```

### Running gitoma Benchmarks

To run the full gitoma benchmark against this rung:

```bash
python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Contributing

We welcome contributions! Please follow these guidelines:

1.  **Fork** the repository.
2.  Create a **new feature branch** (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes with a descriptive message (`git commit -m 'Type: Short description'`).
4.  **Push** to your fork and open a **Pull Request**.
5.  Ensure all tests pass before submitting.

## License

This project is licensed under the MIT License - see the 
[LICENSE](LICENSE) file for details.
