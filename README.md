# gitoma-bench-ladder

[![Build Status](https://github.com/yourusername/gitoma-bench-ladder/actions/workflows/build.yml/badge.svg)](https://github.com/yourusername/gitoma-bench-ladder/actions/workflows/build.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/yourusername/gitoma-bench-ladder/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3.10/)

## Overview
This repository contains a Python implementation demonstrating SQL injection vulnerabilities and their fixes. It's designed to be used with gitoma for security testing and benchmarking.

## Install
Ensure you have Python 3.10+ installed. Then run:
```
pip install -r requirements.txt
```

## Usage
To run the tests locally:
```
python -m pytest -q
```

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
Here's a simple example of how to use the library:
```python
import sqlite3
from src.db import get_conn, init_schema

conn = get_conn()
init_schema(conn)
# ... perform operations ...
```

## Feature
This repository demonstrates:
- SQL injection vulnerabilities in Python applications
- Parameterized query fixes to prevent SQL injection
- Testing infrastructure for security testing