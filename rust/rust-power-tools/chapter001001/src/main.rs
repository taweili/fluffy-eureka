use serde::Deserialize;

#[derive(Deserialize)]
struct Request {
    given_name: String,
    last_name: String
}

fn full_name(given: &str, last: &str) -> String {
    format!("{} {}", given, last)
}

fn main() {
    let r = Request{
        given_name: "John".to_string(),
        last_name: "Doe".to_string()
    };

    dbg!(full_name(&r.given_name, &r.last_name));
    println!("{}", full_name(&r.given_name, &r.last_name));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_deserialize() {
        let actual: Request = serde_json::from_str(r#"{"given_name":"John",
                                                    "last_name":"Doe"}"#).expect("Seralize to work");
        assert_eq!(actual.given_name, "John");
        assert_eq!(actual.last_name, "Doe");
    }
}
