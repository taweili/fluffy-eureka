struct MyPair:
    var first: Int
    var second: Int
    
    fn __init__(inout self, first: Int, second: Int):
        self.first = first
        self.second = second


    fn  __lt__(self, rhs: MyPair) -> Bool:
        return self.first < rhs.first or 
                (self.first == rhs.first and 
                self.second < rhs.second)


def main():
    let myp_one = MyPair(1,2)
    let myp_two = MyPair(2,3)

    print(myp_one < myp_two)
