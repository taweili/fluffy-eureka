package main

import (
	"fmt"
	"math"
)

type Point struct {
	x int
	y int
}

func (p Point) Distance(q Point) int {
	fmt.Printf("D: p %v q %v\n", p, q)
	p.x = p.x + 1
	fmt.Printf("D: p %v q %v\n", p, q)
	return int(math.Hypot(float64(p.x-q.x), float64(p.y-q.y)))
}

func (p *Point) AddXOne() {
	fmt.Printf("A: p %v\n", p)
	p.x = p.x + 1
	fmt.Printf("A: p %v\n", p)
}

func main() {
	p := Point{1, 2}
	q := Point{4, 6}

	fmt.Printf("M: p %v q %v\n", p, q)
	fmt.Println(p.Distance(q))
	fmt.Printf("M: p %v q %v\n", p, q)

	p.AddXOne()
	fmt.Printf("M: p %v q %v\n", p, q)
}
