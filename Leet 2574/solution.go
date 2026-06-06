package main

import "fmt"

func leftRightDifference(nums []int) []int {
	var n int = len(nums)
	result := make([]int, n)

	var total int
	for _, val := range nums {
		total += val
	}

	var leftSum int
	for i, val := range nums {
		total -= val

		if leftSum >= total {
			result[i] = leftSum - total
		} else {
			result[i] = total - leftSum
		}

		leftSum += val
	}

	return result
}

func main() {
	fmt.Println("2574. Left and Right Sum Differences")

	nums := []int{10, 4, 8, 3}
	var result []int = leftRightDifference(nums)
	fmt.Print("[ ")
	for _, num := range result {
		fmt.Printf("%d ", num)
	}

	fmt.Println("]")
}
