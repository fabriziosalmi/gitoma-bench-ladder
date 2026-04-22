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

## Installation and Usage

### Prerequisites

Ensure you have Go installed on your system.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/fabriziosalmi/gitoma-bench-ladder.git
cd gitoma-bench-ladder
```

2. Initialize the Go module and download dependencies:

```bash
go mod tidy
```

### Running Tests

To run the unit tests for this rung, navigate to the specific rung directory and run:

```bash
cd rung-1
go test ./...
```

### Running gitoma Benchmarks

To run the full benchmark suite using gitoma, use the following command:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-1 --reset -y --no-self-review --no-ci-watch
```

For more details on specific rungs, check the documentation or run gitoma with appropriate flags.
