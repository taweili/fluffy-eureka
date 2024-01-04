fn main() {
    let outer_var = 42;
    let closure_annotated = |i: i32| -> i32 { i + outer_var };
    let closure_inferred = |i| i + outer_var;

    println!("{}", closure_annotated(1));
    println!("{}", closure_inferred(1));

}