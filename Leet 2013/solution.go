package main

import (
	"fmt"
	"math"
)

type Point struct {
	X int
	Y int
}

type DetectSquares struct {
	points map[Point]int
}

func Constructor() DetectSquares {
	return DetectSquares{
		points: make(map[Point]int),
	}
}

func (this *DetectSquares) Add(point []int) {
	this.points[Point{X: point[0], Y: point[1]}]++
}

func (this *DetectSquares) Count(point []int) int {
	pt := Point{X: point[0], Y: point[1]}
	var result int

	for key := range this.points {
		if pt.X == key.X || pt.Y == key.Y {
			continue
		}

		dx := math.Abs(float64(key.X - pt.X))
		dy := math.Abs(float64(key.Y - pt.Y))
		if dx != dy {
			continue
		}

		a := this.points[Point{X: key.X, Y: pt.Y}]
		b := this.points[Point{X: pt.X, Y: key.Y}]
		c := this.points[key]
		result += a * b * c
	}

	return result
}

func main() {
	fmt.Println("2013. Detect Squares")

	detectSquares := Constructor()

	detectSquares.Add([]int{3, 10})
	detectSquares.Add([]int{11, 2})
	detectSquares.Add([]int{3, 2})

	fmt.Printf("Count([11,10]) = %d\n", detectSquares.Count([]int{11, 10}))
	fmt.Printf("Count([14,8]) = %d\n", detectSquares.Count([]int{14, 8}))

	detectSquares.Add([]int{11, 2})

	fmt.Printf("Count([11,10]) = %d\n", detectSquares.Count([]int{11, 10}))

}
