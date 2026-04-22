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

## Usage

This project demonstrates how to test cross-file reasoning by introducing subtle signature changes between files. 

### Prerequisites

* Go programming language installed.
* Git installed.

### Running Tests Locally

To run tests for a specific rung:

```bash
cd <rung-directory>
go test ./...
```

### Running with gitoma

To run the full benchmark suite using `gitoma`:

```bash
gitoma run <repo-url> --base <rung-name> --reset -y --no-self-review --no-ci-watch
```
