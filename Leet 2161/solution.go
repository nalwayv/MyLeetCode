package main

import "fmt"

func pivotArray(nums []int, pivot int) []int {
	var lo []int
	var hi []int

	result := make([]int, len(nums))

	var skip int
	for i, num := range nums {
		if num < pivot {
			lo = append(lo, num)
		} else if num > pivot {
			hi = append(hi, num)
		} else {
			skip++
		}

		result[i] = pivot
	}

	var idx int
	for _, l := range lo {
		result[idx] = l
		idx++
	}

	// skip over pivot values
	idx += skip

	for _, h := range hi {
		result[idx] = h
		idx++
	}

	return result
}

func main() {
	fmt.Println("2161. Partition Array According to Given Pivot")

	var nums []int = []int{9, 12, 5, 10, 14, 3, 10}
	var result []int = pivotArray(nums, 10)

	fmt.Print("[")
	for _, r := range result {
		fmt.Printf(" %d ", r)
	}
	fmt.Print("]\n")
}
