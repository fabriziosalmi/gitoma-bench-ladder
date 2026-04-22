# Rung 3 — Python + SQLite: SQL injection in `find_user_by_name`

## Overview

This rung tests a semantic security vulnerability in `src/db.py` where an f-string is used to construct a SQL query, leading to potential SQL injection if user input is not properly sanitized. The goal is to ensure that the function uses parameterised queries to prevent injection attacks.

## The Vulnerability

**Location:** `src/db.py:53` (in `find_user_by_name`)

The original code uses f-string interpolation, which allows an attacker to inject arbitrary SQL commands by supplying malicious input (e.g., using `' OR '1'='1`).

**Example of vulnerability:** `f"SELECT id, name FROM users WHERE name = '{name}'"`

## The Fix

The vulnerability is fixed by switching to parameterised queries provided by the `sqlite3` library, ensuring that user input is treated strictly as data and never as executable SQL.

**Corrected Code Snippet:**
```python
cur = conn.execute(
    "SELECT id, name FROM users WHERE name = ?",
    (name),
)
```

## Testing and Verification

This rung includes adversarial tests in `tests/test_db.py` designed to expose this flaw:

- `test_no_sql_injection`: Tests bypass using `' OR '1'='1'`.
- `test_no_sql_injection_via_comment`: Tests using SQL comment injection like `alice'; --`.

Running tests against the fixed code should result in all injection tests passing, confirming that parameterisation successfully mitigates the risk.

## Running Locally

To run the tests locally:

```bash
cd rung-3
python -m pytest -q
```

## Running gitoma on this rung

To run the automated analysis:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

**Scoring Expectation:**
*   **Pre-fix:** 2 failures (the two injection tests) and 2 passes.
*   **Post-fix:** 4 passes.

## Contributing

This repository focuses on security testing and vulnerability identification. Contributions are welcome in the following areas:

1.  **Bug Reporting:** Report security vulnerabilities found during testing.
2.  **Fixing Issues:** Implement fixes for identified bugs, focusing on secure coding practices (e.g., parameterised queries over string formatting).
3.  **Test Coverage:** Add new adversarial tests to ensure existing vulnerabilities are caught and regressions are prevented.

Please ensure all code changes adhere to secure coding standards. Security findings are highly valued.