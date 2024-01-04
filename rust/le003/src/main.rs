use crate::point::{get_point, Point};
mod point; 

fn main() {
    let a = Point { x: 10, y: 10 };    
    println!("{:?}", a);
    let b = &a;
    println!("{:?}", a);
    println!("{:?}", b);

    let c = Point {x: a.x +10, y: a.y + 200};
    println!("{:?}", c);

    let d = a; 
    println!("{:?}", d);
    // println!("{:?}", a);

    get_point(&d);
    println!("{:?}", d);
}
