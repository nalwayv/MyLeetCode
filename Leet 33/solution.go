package main

import "fmt"

// Search for target within a rotated array and return its index location.
// If not found then -1 is returned.
func search(nums []int, target int) int {
	var lo int = 0
	var hi int = len(nums) - 1

	for lo <= hi {
		var mid int = lo + (hi-lo)/2

		if nums[mid] == target {
			return mid
		}

		if nums[mid] >= nums[lo] {
			if target >= nums[lo] && target < nums[mid] {
				hi = mid - 1
			} else {
				lo = mid + 1
			}
		} else {
			if target > nums[mid] && target <= nums[hi] {
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}
	}

	return -1
}

func main() {
	fmt.Println("33. Search in Rotated Sorted Array")

	var nums []int = []int{4, 5, 6, 7, 0, 1, 2}
	var target int = 0
	var idx int = search(nums, target)

	if idx == -1 {
		fmt.Println("Not found")
	} else {
		fmt.Printf("Target %d was found at index %d\n", target, idx)
	}
}
