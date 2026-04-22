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

```
cd rung-2
cargo check      # must fail pre-fix with E0277
cargo test       # fails pre-fix (bin doesn't build), passes post-fix
```

## Running gitoma on this rung

From minimac:

```
gitoma run https://github.com/fabriziosalmi/gitoma-bench-ladder \
  --base rung-2 --reset -y --no-self-review --no-ci-watch
```

Scoring:

```
python bench/bench_rung.py --rung 2 --pr-url <PR-URL>
```
