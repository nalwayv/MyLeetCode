package main

import (
	"fmt"
	"math"
)

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func intLength(num int) int {
	if num == 0 {
		return 1
	}

	abs := math.Abs(float64(num))
	log := math.Log10(abs)
	floor := math.Floor(log)

	return int(floor) + 1
}

func longestCommonPrefix(arr1 []int, arr2 []int) int {
	seen := make(map[int]bool)

	for i := range arr1 {
		num := arr1[i]

		for num != 0 && !seen[num] {
			seen[num] = true
			num /= 10
		}
	}

	var result int = 0

	for i := range arr2 {
		num := arr2[i]

		for num != 0 && !seen[num] {
			num /= 10
		}

		if num != 0 {
			result = maxInt(result, intLength(num))
		}
	}

	return result
}

func main() {
	fmt.Println("3043. Find the Length of the Longest Common Prefix")

	arr1 := []int{1, 10, 100}
	arr2 := []int{1000}

	var result int = longestCommonPrefix(arr1, arr2)
	fmt.Printf("Longest common prefix for [1 10 100] and [1000] is %d\n", result)
}
