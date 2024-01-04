#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

fn main() {
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age};

    println!("{:?}", peter);
}
