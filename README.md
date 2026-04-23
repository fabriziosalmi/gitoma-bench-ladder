# gitoma-bench-ladder

## Overview

This repository contains a benchmark for testing semantic security vulnerabilities in Python applications using SQLite. The focus is on preventing SQL injection attacks through proper parameter binding techniques.

## Project Structure

```
LICENSE
README.md
SECURITY.md
golden.json
pyproject.toml
src/
  __init__.py
  db.py          # Database operations with SQL injection vulnerability
tests/
  __init__.py
  test_db.py     # Tests for SQL injection vulnerability
```

## Installation

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

### Running Tests

To run the tests, use pytest:

```bash
cd rung-3
python -m pytest -q
```

Expected results (pre-fix): 2 fail (the two injection tests), 2 pass.
Expected results (post-fix): 4 pass.

### Running gitoma

To run gitoma on this benchmark, use the following command from minimac:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder 
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

### Scoring

Use the following command to score your fix:

```bash
python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## Contributing

For contribution guidelines, please refer to SECURITY.md.

## License

The project is licensed under the terms of the LICENSE file.