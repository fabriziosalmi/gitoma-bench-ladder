# gitoma-bench-ladder

[![Build Status](https://github.com/fabriziosalmi/gitoma-bench-ladder/actions/workflows/test.yml/badge.svg)](https://github.com/fabriziosalmi/gitoma-bench-ladder/actions/workflows/test.yml)
[![License](https://badgen.net/maven/license/mvnrepository.com/com.example.gitoma-bench-ladder/0.1.0)](https://github.com/fabriziosalmi/gitoma-bench-ladder/blob/main/LICENSE)
[![Python Version](https://badgen.net/badge/python/3.8/blue)](https://www.python.org/downloads/release/python-380/)

## Overview
This repository contains a benchmark for testing SQL injection vulnerabilities in Python applications using SQLite. It demonstrates how to identify and fix common security issues in database queries.

## Install
To run the benchmarks, you'll need Python 8+ installed.

1. Clone the repository:
```bash
git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
```
2. Navigate to the project directory:
```bash
cd gitoma-bench-ladder
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
To run the tests locally:
```bash
python -m pytest -q
```

Expected results (before fixing the SQL injection bug):
- 2 tests fail (the two injection tests)
- 2 tests pass

Expected results (after fixing the SQL injection bug):
- All 4 tests pass

## Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add tests for your changes
5. Commit your changes
6. Push to your branch and create a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Example
Here's an example of how to fix the SQL injection vulnerability in `src/db.py`:

```python
# Before (vulnerable)
cur = conn.execute(f"SELECT id, name FROM users WHERE name = '{name}'")

# After (fixed)
cur = conn.execute("SELECT id, name FROM users WHERE name = ?", (name,))
```

## Feature
This benchmark demonstrates how to identify and fix SQL injection vulnerabilities in Python applications using SQLite. It includes:
- Two adversarial tests that demonstrate how SQL injection can be used to bypass security checks
- A fix that uses parameterised queries to prevent SQL injection