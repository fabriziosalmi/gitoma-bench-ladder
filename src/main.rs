use calc::divide;

fn main() {
    let x = divide(10, 2);
    match x {
        Ok(value) => println!("10/2 = {}", value),
        Err(e) => eprintln!("Error: {}", e),
    }
}