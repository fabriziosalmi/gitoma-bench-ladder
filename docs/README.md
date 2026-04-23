# gitoma-bench-ladder

## Project Overview
This repository contains a series of benchmarking rungs for the gitoma tool, designed to test various aspects of code quality and security. The current focus is on the third rung, which addresses a SQL injection vulnerability in the `find_user_by_name` function.

## Key Features
- **SQL Injection Fix**: The `find_user_by_name` function has been updated to use parameterized queries, preventing SQL injection attacks.
- **Testing**: Comprehensive tests are included to ensure the correctness of the implementation and to catch any regressions.
- **Documentation**: This README provides detailed instructions on how to set up, run, and contribute to the project.

## Getting Started
### Installation
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
4. Run the tests:
   ```bash
python -m pytest -q
   ```

### Running Locally
To run the tests locally:
```bash
cd rung-3
python -m pytest -q
```

Expected results: All tests should pass after the SQL injection fix.

## Contributing
### How to Contribute
1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they are well-documented.
4. Run the tests to verify that your changes haven't broken anything.
5. Commit your changes and push them to your branch.
6. Open a pull request from your branch to the main repository.

### Code of Conduct
Please follow the standard code of conduct for open-source projects. Be respectful, collaborative, and helpful.

### Testing
All changes must be accompanied by tests. Ensure that your tests cover edge cases and verify the correctness of your implementation.

## License
This project is licensed under the MIT License - see the LICENSE file for details.