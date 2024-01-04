#![feature(trace_macros)]
#![feature(log_syntax)]

use crate::greeting::base_greeting_fn;

#[macro_use]
mod greeting;
fn main() {
    trace_macros!(true);
    let greet = greeting!("Sam", "Heya");
    let greet_with_default = greeting!("Dave");
    let greet_with_test: String = greeting!(test "Tim");
    trace_macros!(false);

    println!("{}", greet);
    println!("{}", greet_with_default);
    println!("{}", greet_with_test);
}
