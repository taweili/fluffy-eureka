#[macro_use]
extern crate hello_world_macro;

#[derive(Hello, UpperCaseName)]
struct Example;

impl Example {
    fn bye_world(&self) {
        println!("Bye World!");
    }
}


#[derive(Hello)]
enum Pet {
    Cat,
}

fn main() {
    let e = Example{};
    e.hello_world();
    e.bye_world();
    e.uppercase();

    let p = Pet::Cat;
    p.hello_world();
}