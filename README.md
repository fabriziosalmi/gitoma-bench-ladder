# Rung 1 — cross-file Go signature mismatch

## What this rung tests

Cross-file reasoning. The fix lives in one file, but deriving the
right fix requires READING a second file to learn the
recently-changed signature.

## The injected bug

`server/server.go:27` — `s.users.Get(id)` is called old-style, 
expecting one return value. `store.UserStore.Get` now returns
`(string, bool)`. The file does not compile.

## The fix

Update `server.Greet` to:

1. Capture both return values: `name, ok := s.users.Get(id)`
2. Branch on `ok`: if false, return "Hello, stranger!"
3. Otherwise return the formatted greeting

Single-file patch in `server/server.go`. But the worker MUST have
read `store/store.go` to know the new signature + the meaning of the bool,
otherwise the patch will be a guess.

## Running the test locally

```
cd rung-1
go test ./...
```

Expected (pre-fix): compile error on `server/server.go:27` — "too
many return values". `go test` exits non-zero with the compile
failure.

Expected (post-fix): both tests pass, `go test ./...` is green.

## Running gitoma on this rung

From minimac:

```
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-1 --reset -y --no-self-review --no-ci-watch
```

Scoring from this repo:

```python bench/bench_rung.py --rung 1 --pr-url <url-gitoma-printed>
```

## Installation

To run the benchmarks, ensure you have Go installed.

1. Clone the repository:

```bash
git clone <repository_url>
cd gitoma-bench-ladder
```

2. Ensure your Go environment is set up and dependencies are fetched:

```bash
got mod tidy
```

## Usage

This project is designed to test cross-file reasoning capabilities in Go code by simulating a CI/CD environment using `gitoma`.

1. **Run Tests Locally**: Navigate to a specific rung directory (e.g., `rung-1`) and run tests:

   ```bash
   cd rung-1
   go test ./...
   ```

2. **Run Benchmarks with gitoma**: Use the `gitoma run` command to execute benchmarks against specific rungs:

   ```bash
   gitoma run <url> --base <rung_name> --reset -y --no-self-review --no-ci-watch
   ```

3. **Scoring**: Use the provided Python script to calculate the score based on the output:

   ```bash
   python bench/bench_rung.py --rung <rung_number> --pr-url <url-gitoma-printed>
   ```

## Example

This section demonstrates how to test the fix described above.

**Scenario**: Testing Rung 1 (cross-file signature mismatch).

*   **Goal**: Ensure that updating `server/server.go` correctly handles the new signature from `store/store.go`.
*   **Action**: Apply the fix described in the README to `server/server.go`.
*   **Verification**: Run tests and gitoma benchmarks to confirm successful compilation and scoring.

*Note: Specific file paths for tests and setup depend on the exact rung being tested.*