# gitoma-bench-ladder

## Overview
This repository contains a benchmark for testing SQL injection vulnerabilities in Python applications using SQLite. It includes a sample implementation with known security issues and test cases to demonstrate the vulnerability.

## Installation
To run this benchmark, you'll need Python 3.7+ installed. Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage Examples
### Running Tests
To run the test suite, use pytest:

```bash
cd rung-3
test -q
```

### Running Locally
To run the benchmark locally, use:

```bash
cd rung-3
python -m pytest -q
```

## Contributing Guidelines
Contributions are welcome! Please follow these guidelines:
- Fork the repository and create a new branch for your feature or bugfix.
- Make sure tests pass before submitting a pull request.
- Add documentation for any new features or changes.

## Licensing Information
This project is licensed under the MIT License. See the LICENSE file for more information.

## Running gitoma
From minimac:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \n  --base rung-3 --reset -y --no-self-review --no-ci-watch
```

Scoring:

```bash
python bench/bench_rung.py --rung 3 --pr-url <PR-URL>
```

## License
MIT License

Copyright (c) 2023 Fabrizio Salmi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.