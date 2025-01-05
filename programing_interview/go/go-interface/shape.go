package main

import "fmt"

type shape interface {
	area() int
}

type square struct {
	sideLength int
}

type rectangle struct {
	height int
	width  int
}

func (s square) area() int {
	return s.sideLength * s.sideLength
}

func (r rectangle) area() int {
	return r.height * r.width
}

func printArea(s shape) {
	fmt.Println(s.area())
}

func main() {
	sqq := square{10}
	rect := rectangle{10, 20}
	printArea(sqq)
	printArea(rect)
}
