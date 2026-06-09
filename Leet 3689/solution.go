package main

import "fmt"

func maxTotalValue(nums []int, k int) int64 {
	if len(nums) == 0 {
		return 0
	}

	// get the min and the max values from the slice
	lo := nums[0]
	hi := nums[0]
	for i := 1; i < len(nums); i++ {
		lo = min(lo, nums[i])
		hi = max(hi, nums[i])
	}

	return int64((hi - lo) * k)
}

func main() {
	fmt.Println("3689. Maximum Total Subarray Value I")

	nums := []int{1, 3, 2}
	var result int64 = maxTotalValue(nums, 2)
	fmt.Printf("Result: %d\n", result)
}
