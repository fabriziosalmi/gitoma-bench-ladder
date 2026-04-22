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

```bash
cd rung-0
python -m pytest -q
```

Expected (pre-fix): 2 fail, 1 pass. The buggy line breaks both
`test_average_of_three` (wrong result) and `test_average_single`
(ZeroDivisionError). `test_average_empty_raises` passes because the
elrurn runs before the buggy arithmetic.

Expected (post-fix): 3 pass.

## Running gitoma on this rung

From minimac:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-0 --reset -y
```

Gitoma will create a working branch off `rung-0`, fix the bug, open
a PR targeting `rung-0`.

## Scoring

From this repo's `main` branch:

```bash
python bench/bench_rung.py --rung 0 --pr-url <url-printed-by-gitoma>
```

## Usage

This repository demonstrates the core functionality of `gitoma` by testing a single, isolated bug fix.

1. **Clone the repository:**
   ```bash
   git clone <repo_url>
   cd gitoma-bench-ladder
   ```
2. **Run locally:**
   To test the current state of a rung:
   ```bash
   python -m pytest -q
   ```
3. **Use gitoma:**
   To automatically fix and propose a PR for a rung:
   ```bash
   gitoma run <rung_name> --base <rung_name> --reset -y
   ```

## Contributing

Contributions are welcome! If you find a bug in the testing setup or want to improve the `gitoma` workflow, please open an issue or submit a pull request.

*   Report bugs clearly, including steps to reproduce and expected vs. actual behavior.
*   Propose improvements to the testing harness or documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Example

This example shows how to run the automated process for a specific rung:

```bash
# Example: Running gitoma on 'rung-0'
python bench/bench_rung.py --rung 0 --pr-url <output_url>
```

## Features

This repository serves as a benchmark for the `gitoma` tool. Future features might include:

*   Adding more complex test suites (multiple files/dependencies).
*   Implementing cross-file reasoning capabilities.
*   Supporting different testing frameworks.

