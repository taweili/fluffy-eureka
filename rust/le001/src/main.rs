fn main() {
    // use std::mem;

    let print = || println!("hello");
    print();

    let mut count = 0;

    let mut inc = || {
        count += 1;
        println!("count: {}", count);
    };

    inc();
    inc();
    inc();

}
