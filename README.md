# Rung 2 — Rust: Result handling in caller after signature change

## What this rung tests

Rust-flavoured compile failure. The library `calc` exposes
`divide(a, b) -> Result<i32, String>`; the binary `main.rs` still
tries to `println!` the Result directly as `{}`. Rust rejects that
at compile time — `Result<T, E>` does not implement `Display`.

This is the Rust analogue of rung-1: the fix lives in one file
(`src/main.rs`) but deriving the right fix requires reading
`src/calculator.rs` to see the Result-returning signature.

## The injected bug

`src/main.rs:21` — `println!("10/2 = {}", x)` where `x` is
`Result<i32, String>`. Rustc emits:

```
error[E0277]: `Result<i32, String>` doesn't implement `std::fmt::Display`
```

## Acceptable fixes

Any of the standard Rust Result-handling idioms is fine:

```rust
// option A — match
match divide(10, 2) {
    Ok(v) => println!("10/2 = {v}"),
    Err(e) => eprintln!("error: {e}"),
}

// option B — unwrap / expect (brittle but valid)
let x = divide(10, 2).unwrap();
println!("10/2 = {x}");

// option C — ? propagation (requires main to return Result)
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let x = divide(10, 2).map_err(|e| e as Box<dyn std::error::Error>)?;
    println!("10/2 = {x}");
    Ok(())
}
```

Whichever is picked, the three tests in `tests/calculator_test.rs`
must stay green.

## Running locally

```bash
cd rung-2
cargo check      # must fail pre-fix with E0277
cargo test       # fails pre-fix (bin doesn't build), passes post-fix
```

## Running gitoma on this rung

From minimac:

```bash
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-2 --reset -y --no-self-review --no-ci-watch
```

Scoring:

```bash
python bench/bench_rung.py --rung 2 --pr-url <PR-URL>
```

## Installation

To run this project locally, ensure you have Rust installed.

1. Clone the repository:
```bash
git clone <repository_url>
cd gitoma-bench-ladder
```

2. Build and test (for development):
```bash
cargo check
cargo test
```

## Usage

This project is a benchmark rung for testing Rust's result handling.

*   **Testing:** Run `cargo test` to verify that the fix maintains test coverage.
*   **Benchmarking:** Use `gitoma run` to score this rung against others.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to submit pull requests.

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Example

Example of fixing the issue (Option A):

```rust
match divide(10, 2) {
    Ok(v) => println!("10/2 = {v}"),
    Err(e) => eprintln!("error: {e}"),
}
```

## Features

This rung specifically tests the compiler's strictness regarding Rust's `Result` type and its inability to implicitly convert to `Display`.

*   Tests the compiler's strictness on Result types.
*   Validates that idiomatic error handling patterns are accepted.
