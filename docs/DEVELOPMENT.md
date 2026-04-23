# Development Guide

## Setting Up the Environment
1. Ensure you have Python 3.8+ installed.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up a virtual environment (optional but recommended): `python -m venv venv` and activate it.

## Running Tests
1. Navigate to the `tests/` directory.
2. Run the tests using: `python -m pytest`

## Linting and Formatting
1. Use `black` to format your code: `black src/`
2. Use `flake8` for linting: `flake8 src/`

## Committing Changes
1. Write clear and concise commit messages.
2. Use the conventional commits format: `feat(scope): description` or `fix(scope): description`.