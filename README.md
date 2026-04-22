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

### Prerequisites

* Go programming language (version 1.18 or newer)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
   cd gitoma-bench-ladder
   ```

2. **Initialize Go modules and download dependencies:**
   ```bash
   go mod tidy
   ```

3. **Run tests (optional):**
   To verify the current state of the project, run the tests:
   ```bash
   go test ./...
   ```

4. **Running benchmarks (using gitoma):**
   To run the automated benchmarking suite, use the `gitoma` tool:
   ```bash
   gitoma run <URL_TO_THIS_REPO> --base <rung_name> --reset -y --no-self-review --no-ci-watch
   ```

Note: Replace `<URL_TO_THIS_REPO>` with the actual URL of this repository if running externally, or use the local path depending on your gitoma setup.
