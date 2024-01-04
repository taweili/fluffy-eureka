use private_macro::private;

private!(
    struct Example {
        string_value: String, 
        number_value: i32,
    }
);

fn main() {
    let e = Example {
        string_value: "Hello, world!".to_string(),
        number_value: 1,
    };

    let str_value = e.get_string_value();
    let num_value = e.get_number_value();

    println!("{} {}", str_value, num_value);    
}
