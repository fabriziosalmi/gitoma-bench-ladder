# gitoma-bench-ladder

[![Project Status](https://img.shields.io/badge/project_status-actively%20developed-green.svg)](https://img.shields.io/badge/project_status-actively%20developed-green.svg)
[![Build Status](https://img.shields.io/badge/build-passing-green.svg)](https://img.shields.io/badge/build-passing-green.svg)
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-green.svg)](https://img.shields.io/badge/coverage-100%25-green.svg)

## Install

Ensure you have Python 3.10+ installed. Then run:

```bash
pip install -r requirements.txt
```

## Usage

To run tests:

```bash
cd rung-3
python -m pytest -q
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b my-feature`)
3. Make your changes
4. Add tests for your changes
5. Commit your changes (`git commit -m "Add my feature"`)
6. Push to the branch (`git push origin my-feature`)
7. Create a pull request

## License

This project is licensed under the MIT License.

## Example

Here's an example of how to use the library:

```python
import sqlite3
from src.db import get_conn, init_schema

conn = get_conn()
init_schema(conn)
```

## Feature

This project demonstrates a SQL injection vulnerability in the `find_user_by_name` function. The goal is to fix this vulnerability by using parameterized queries.