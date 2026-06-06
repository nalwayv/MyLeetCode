package main

import (
	"fmt"
	"math"
)

func absInt(a int) int {
	return int(math.Abs(float64(a)))
}

func minMirrorPairDistance(nums []int) int {
	// [num] index
	distances := make(map[int]int)
	minDistance := math.MaxInt

	for i := range nums {
		var num int = nums[i]

		// get reverse number
		var reverse int = 0
		for num > 0 {
			tmp := num % 10
			reverse = reverse*10 + tmp
			num /= 10
		}

		// reset num
		num = nums[i]

		// if the reverse of num is in the map update min distance between indexes
		if idx, ok := distances[num]; ok {
			minDistance = min(minDistance, absInt(i-idx))
		}

		// add reverse and current index to map
		distances[reverse] = i

	}

	// no min dist found
	if minDistance == math.MaxInt {
		return -1
	}

	return minDistance
}

func example1() {
	var nums []int = []int{12, 21, 45, 33, 54}
	var distance int = minMirrorPairDistance(nums)
	fmt.Printf("{12, 21, 45, 33, 54} min distance = %d\n", distance)
}

func example2() {
	var nums []int = []int{120, 21}
	var distance int = minMirrorPairDistance(nums)
	fmt.Printf("{120, 21} min distance = %d\n", distance)
}

func main() {
	fmt.Println("3761. Minimum Absolute Distance Between Mirror Pairs")
	example1()
	example2()
}
