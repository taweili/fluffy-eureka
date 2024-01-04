#[derive(Debug)]
pub struct Point {
    pub x: i32,
    pub y: i32,
}

pub fn get_point(p: &Point) {
    println!("get_point: {:?}", p);
}