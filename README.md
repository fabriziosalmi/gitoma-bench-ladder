# gitoma-bench-ladder

## Project Overview

This repository contains a benchmark for testing semantic security vulnerabilities in Python applications using SQLite. The focus is on preventing SQL injection attacks through proper parameter binding techniques.

## Features

- Tests for SQL injection vulnerabilities
- Example of a vulnerable query and its fix
- Demonstration of parameterized queries for secure database interactions

## Installation

To install the project, ensure you have Python installed. Then run:

```bash
pip install -r requirements.txt
```

## Usage

To run the tests, use:

```bash
cd rung-3
python -m pytest -q
```

## Contributing

Contributions are welcome! Please review the existing tests and consider adding new ones to further explore security vulnerabilities.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Example

Here's an example of a vulnerable query and its secure fix:

### Vulnerable Code
```python
f"SELECT id, name FROM users WHERE name = '{name}'"
```

### Secure Fix
```python
cur = conn.execute("SELECT id, name FROM users WHERE name = ?", (name,))
```

## Feature

This project demonstrates the importance of parameterized queries in preventing SQL injection attacks. The example shows how to correctly bind parameters to avoid security vulnerabilities.