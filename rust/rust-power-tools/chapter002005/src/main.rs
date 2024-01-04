#![feature(trace_macros)]

macro_rules! hello_world {
    ($something:ident) => {
        impl $something {
            fn hello_world(&self) {
                println!("Hello world")
            }
        }
    };
}

struct Example {}

trace_macros!(true);
hello_world!(Example);
trace_macros!(false);

fn main() {
    let e = Example {};
    e.hello_world(); // prints "Hello world"
}