//! Tiny calculator — the stable side of rung-2.
//!
//! `divide` was recently hardened from panicking on divide-by-zero to
//! returning `Result<i32, String>`. Callers that still treat the
//! return as a plain `i32` fail to compile — `Result` does not
//! implement `Display`, so `println!("{}", divide(a,b))` is rejected.

/// Return `Ok(a/b)` on success, `Err(message)` when `b == 0`.
pub fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        return Err(format!("divide by zero: {}/{}", a, b));
    }
    Ok(a / b)
}
