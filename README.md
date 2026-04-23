# gitoma-bench-ladder

## 🧪 Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
```bash
 git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
 cd gitoma-bench-ladder
```
2. Install dependencies:
```bash
 pip install -r requirements.txt
```

## 🚀 Usage

### Running Tests
To run the test suite:
```bash
cd tests
python -m pytest -q
```

### Running Locally
To run the benchmark locally:
```bash
python -m pytest
```

## ✍️ Contributing

### Contribution Guidelines
1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure tests pass.
4. Submit a pull request with a clear description of your changes.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📌 Example
```python
# Example usage of the benchmark
from src.db import get_conn, init_schema

conn = get_conn()
init_schema(conn)
# Run your benchmark logic here
```

## 🚀 Features
- SQL injection vulnerability detection
- Automated test suite for security checks
- Easy-to-use benchmarking framework
