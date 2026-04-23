# Contributing Guide

## Project Structure

The repository follows a standard Python project structure:

- `README.md`: Overview of the project
- `golden.json`: Expected test results for validation
- `pyproject.toml`: Project configuration file
- `src/`: Source code directory
  - `__init__.py`: Initializes the package
  - `db.py`: Database interaction logic
- `tests/`: Test directory
  - `__init__.py`: Initializes the tests
  - `test_db.py`: Tests for database functionality

## Workflows

### Development Workflow
1. Clone the repository: `git clone <repository-url>`
2. Create a new branch for your feature or bug fix: `git checkout -b <branch-name>`
3. Make your changes and ensure they follow the project structure
4. Run tests to verify your changes: `pytest`
5. Commit your changes and push them to your branch: `git commit` and `git push`

### Testing Workflow
1. Ensure you have Python installed (version specified in `pyproject.toml`)
2. Install dependencies: `poetry install`
3. Run tests using `pytest` to ensure all test cases pass

## Code Style and Standards
- Follow PEP8 style guidelines for Python code
- Use descriptive variable names and function signatures
- Write clear comments explaining complex logic

## Submitting Changes
1. Push your changes to your branch on the remote repository
2. Create a pull request (PR) targeting the main branch
3. Ensure all tests pass and there are no code style issues
4. Provide a clear description of your changes in the PR message

## License
This project is licensed under the MIT License - see the LICENSE file for details.