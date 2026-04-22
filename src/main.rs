// NOTE (reader): this file no longer compiles. `divide` returns
// `Result<i32, String>`, but the code below tries to pass the
// Result to `println!` via `{}`, which requires `Display`. Result
// does not implement it.
//
// Fixing requires handling the Result explicitly. Typical patterns:
//   * `.unwrap()` / `.expect("reason")` — panics on Err; fine for
//     a demo main but brittle in real code.
//   * `match` on the Result, printing either the value or the error.
//   * `?` propagation if `main` returns `Result<(), Box<dyn Error>>`.
//
// Whichever you pick, the tests in `tests/calculator_test.rs` MUST
// keep passing — they call `divide` directly and do not depend on
// `main`'s behaviour. If you change the fix in a way that alters
// `calculator.rs`, the tests will catch it.

use calc::divide;

fn main() {
    let x = divide(10, 2);
    println!("10/2 = {}", x);
}
