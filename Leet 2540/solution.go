package main

import "fmt"

// Get the minimum common value between nums1 and nums2.
// Returns ever min value or -1 if none is found.
func getCommon(nums1 []int, nums2 []int) int {
	var i int = 0
	var j int = 0

	for i < len(nums1) && j < len(nums2) {
		if nums1[i] == nums2[j] {
			return nums1[i]
		} else if nums1[i] < nums2[j] {
			i++
		} else {
			j++
		}
	}

	return -1
}

func main() {
	fmt.Println("2540. Minimum Common Value")

	nums1 := []int{1, 2, 3}
	nums2 := []int{2, 4}

	fmt.Printf("Min common value between nums1 and nums2 is: %d\n", getCommon(nums1, nums2))
}
