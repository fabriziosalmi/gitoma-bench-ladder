# Rung 0 — single file, single bug

## What this rung tests

The most basic worker-fix-testpass loop: gitoma reads one broken
Python file, spots the bug, proposes a one-line fix, pytest passes.

**No panel complexity, no cross-file reasoning, no dependency graph.**

If this rung does not pass, nothing above it will — full stop.

## The injected bug

`calc.py:18` — `average()` divides by `len(nums) - 1` instead of
`len(nums)`. Classic off-by-one.

The failing test `test_average_of_three` pins the bug.

## Running the test locally

```
cd rung-0
python -m pytest -q
```

Expected (pre-fix): 2 fail, 1 pass. The buggy line breaks both
`test_average_of_three` (wrong result) and `test_average_single`
(ZeroDivisionError). `test_average_empty_raises` passes because the
early-return runs before the buggy arithmetic.

Expected (post-fix): 3 pass.

## Running gitoma on this rung

From minimac:

```
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-0 --reset -y
```

Gitoma will create a working branch off `rung-0`, fix the bug, open
a PR targeting `rung-0`.

## Running gitoma on this rung (Installation)

To run tests or use the toolchain, install the required dependencies:

```bash
pip install -r requirements-test.txt
```

## Usage Examples for calc.py
This section demonstrates how to use the functions available in `calc.py`.

### Basic Average Calculation

To calculate the average of a list of numbers, use the `average` function:

```python
from calc import average

numbers = [1, 2, 3, 4, 5]
result = average(numbers)
print(f"The average is: {result}")  # Output: The average is: 3.0

empty_list = []
# This will raise a ValueError if not handled internally by the function
# average(empty_list)
```

### Calculating Average for a Single Number

Use `average` with a single-element list:

```python
from calc import average

single_number = [42]
result = average(single_number)
print(f"The average is: {result}")  # Output: The average is: 42
```

## Contributing

We welcome contributions! If you find a bug, have a feature idea, or want to improve the tooling,
please feel free to open an issue or submit a pull request.

### How to Contribute

1. **Fork the repository:** Create your own fork of this repository.
2. **Clone locally:** Clone your fork to your local machine.
3. **Create a new branch:** Create a new branch for your changes (`git checkout -b feature/my-new-thing`).
4. **Make your changes:** Implement the fix or feature.
5. **Test:** Ensure your changes pass all existing tests (run `python -m pytest`).
6. **Commit:** Commit your changes with a descriptive message.
7. **Pull Request (PR):** Open a Pull Request targeting the main branch. Please ensure your PR includes relevant tests if you are changing test logic.

### Code of Conduct

We are committed to maintaining a friendly and inclusive development environment. Please read our [CODE_OF_CONDUCT.md] (if one exists, otherwise add one) for guidelines on respectful interaction.
