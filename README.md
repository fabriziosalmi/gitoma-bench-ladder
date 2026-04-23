# gitoma-bench-ladder

## 🧪 Project Overview

This repository contains a benchmark for testing SQL injection vulnerabilities in Python applications using SQLite. It demonstrates how to identify and fix common security issues in database interactions.

## 📦 Features

- Demonstrates SQL injection vulnerability
- Shows canonical fix using parameterized queries
- Includes adversarial test cases
- Provides complete testing infrastructure

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Run tests to see the vulnerability:
   ```bash
   cd gitoma-bench-ladder
   python -m pytest tests/test_db.py
   ```
2. Apply the fix in src/db.py and re-run tests:
   ```bash
   python -m pytest tests/test_db.py
   ```

## ✍️ Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📚 Example

Here's an example of vulnerable code:
```python
query = f"SELECT id, name FROM users WHERE name = '{name}'"
```

And the fixed version:
```python
cur = conn.execute("SELECT id, name FROM users WHERE name = ?", (name,))
```

## 🚀 Running with gitoma

To run this benchmark through gitoma:
```
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder 
  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

[![Build Status](https://github.com/fabriziosalmi/gitoma-bench-ladder/actions/workflows/test.yml/badge.svg)](https://github.com/fabriziosalmi/gitoma-bench-ladder/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)