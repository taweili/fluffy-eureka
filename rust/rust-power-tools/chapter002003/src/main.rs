use std::ops::{Add, Sub};

#[derive(Debug)]
struct Account {
    money: u32,
}

impl Account {
    fn add(&mut self, money: u32) {
        self.money = self.money.add(money);
    }
    fn sub(&mut self, money: u32) {
        self.money = self.money.sub(money);
    }
}

macro_rules! exchange {
    (Give $amount:literal to $name:ident) => {
        $name.add($amount);
    };
    (Take $amount:literal from $name:ident) => {
        $name.sub($amount);
    };
    (Give $amount:literal to $receiver:ident from $giver:ident) => {
        $giver.sub($amount);
        $receiver.add($amount);
    }
}

fn main() {
    let mut the_poor = Account { money: 10 };
    let mut the_rich: Account = Account { money: 100 };
    println!("Poor: {:?} Rich: {:?}", the_poor, the_rich);

    exchange!(Give 10 to the_poor);
    println!("Poor: {:?} Rich: {:?}", the_poor, the_rich);

    exchange!(Take 10 from the_rich);
    println!("Poor: {:?} Rich: {:?}", the_poor, the_rich);

    exchange!(Give 10 to the_poor from the_rich);
    println!("Poor: {:?} Rich: {:?}", the_poor, the_rich);
}