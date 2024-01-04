use builder_macro::Builder;

#[derive(Builder)]
struct Gleipnir {
    roots_of: String,
}

fn main() {}

#[cfg(test)]
mod tests {

    #[test]
    fn should_generate_builder_for_struct_with_no_properties() {
        use builder_macro::Builder;
        #[derive(Builder)]
        struct ExampleStructNoFields {}

        let _ = ExampleStructNoFields::builder().build();
    }

    #[test]
    fn should_generate_builder_for_struct_with_one_property () {
        use builder_macro::Builder;

        #[derive(Builder)]
        struct Gleipnir {
            roots_of: String,
        }

        let gleipnir = Gleipnir::builder().roots_of("mountains".to_string()).build();

        assert_eq!(gleipnir.roots_of, "mountains");
    }
}