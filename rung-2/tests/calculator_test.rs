use calc::divide;

#[test]
fn divides_cleanly() {
    assert_eq!(divide(10, 2), Ok(5));
}

#[test]
fn reports_zero_denom() {
    match divide(10, 0) {
        Ok(_) => panic!("expected error on divide-by-zero"),
        Err(msg) => assert!(
            msg.contains("divide by zero"),
            "unexpected error message: {msg:?}"
        ),
    }
}

#[test]
fn negative_inputs_work() {
    assert_eq!(divide(-10, 2), Ok(-5));
}
