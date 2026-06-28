package main

import "fmt"

func MaximumLength(nums []int) int {
	frequency := make(map[int]int)
	for _, num := range nums {
		frequency[num]++
	}

	result, ok := frequency[1]
	if ok {
		frequency[1] = 0
	}

	if result%2 == 0 {
		result--
	}

	for key := range frequency {
		var count int
		num := key

		for frequency[num] > 1 {
			count += 2
			num *= num
		}

		if _, ok := frequency[num]; ok {
			count += 1
		} else {
			count -= 1
		}

		result = max(result, count)
	}

	return result
}

func main() {
	fmt.Println("3020. Find the Maximum Number of Elements in Subset")

	var result1 int = MaximumLength([]int{5, 4, 1, 2, 2})
	fmt.Printf("Result: %d\n", result1)

	var result2 int = MaximumLength([]int{1, 3, 2, 4})
	fmt.Printf("Result: %d\n", result2)
}
