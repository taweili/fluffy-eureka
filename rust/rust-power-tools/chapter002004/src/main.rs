// #![feature(trace_macros)]

fn add_one(n:i32) -> i32 {
    n + 1
}

fn stringify(n:i32) -> String {
    n.to_string()
}

fn prefix_with(prefix: &str) -> impl Fn(String) -> String + '_ {
    move |x| format!("{}{}", prefix, x)
}

fn subfix_with(subfix: &str) -> impl Fn(String) -> String + '_ {
    move |x| format!("{}{}", x, subfix)
}
fn compose_two<FIRST, SECOND, THIRD, F, G>(f: F, g: G) ->
    impl Fn(FIRST) -> THIRD
    where   F: Fn(FIRST) -> SECOND,
            G: Fn(SECOND) -> THIRD {
                move |x| g(f(x))
            }

macro_rules! compose {
    ($last:expr) => { $last };
    ($head:expr, $($rest:expr),+) => {
        compose_two($head, compose!($($rest),+))
    }
}

fn main() {
    // trace_macros!(true);
    let compose = compose!(
        add_one, 
        stringify,
        prefix_with("Hello, "),
        subfix_with(" persons")
    );
    // trace_macros!(false);

    println!("{}", compose(10));
}
