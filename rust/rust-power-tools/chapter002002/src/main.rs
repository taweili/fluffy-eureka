struct FirstName {
    value: String,
}
struct LastName {
    value: String,
}

struct Age {
    value: i32,
}

struct Pay {
    value: i32,
}

macro_rules! generate_get_value {
    ($struct_type:ident) => {
        generate_get_value!($struct_type, String);
    };
    ($struct_type:ident,$return_type:ty) => {
        impl $struct_type {
            pub fn get_value(&self) -> &$return_type {
                &self.value
            }
        }
    }
}

generate_get_value!(FirstName);
generate_get_value!(LastName);
generate_get_value!(Age, i32);
generate_get_value!(Pay, i32);

fn calculate_raise(first_name: FirstName, last_name: LastName, age: Age, pay: Pay) -> Pay {
    if first_name.get_value() == "John" && last_name.get_value() == "Doe" {
        if age.get_value() > &40 {
            Pay { value: pay.get_value() * 3 }
        } else {
            Pay { value: pay.get_value() * 2}
        }            
    } else {
        Pay { value: pay.get_value() * 1}
    }
}
fn main() { 
    let first_name = FirstName { value: "Johnny".to_string() };
    let last_name = LastName { value: "Doe".to_string() };
    let age = Age { value: 45 };
    let pay = Pay { value: 3000 };
    
    let raised_pay = calculate_raise(first_name, last_name, age, pay);

    print!("Raised Pay: {}", raised_pay.get_value())
}
