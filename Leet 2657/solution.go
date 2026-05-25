package main

import "fmt"

// Return the minimum of two integers
func minInt(num1 int, num2 int) int {
	if num1 < num2 {
		return num1
	}
	return num2
}

// Return the prefix common array between A and B (generic over comparable types)
func findThePrefixCommonArray[T comparable](A []T, B []T) []int {
	// each array contains distinct integers from 1 to n,
	// so if the same integer appears in both arrays,
	// it will be counted as a common integer

	length := minInt(len(A), len(B))
	result := make([]int, length)
	tally := make(map[T]int)

	var count int = 0
	for i := 0; i < length; i++ {
		tally[A[i]]++
		if tally[A[i]] == 2 {
			count++
		}

		tally[B[i]]++
		if tally[B[i]] == 2 {
			count++
		}

		result[i] = count
	}

	return result
}

func printArr[T any](message string, arr []T) {
	fmt.Printf("%s: [", message)
	for i := range arr {
		fmt.Printf(" %v ", arr[i])
	}
	fmt.Printf("]\n")
}

func main() {
	fmt.Println("2657. Find the Prefix Common Array of Two Arrays")

	arrayA := []int{1, 3, 2, 4}
	arrayB := []int{3, 1, 2, 4}

	var result []int = findThePrefixCommonArray(arrayA, arrayB)

	printArr("A", arrayA)
	printArr("A", arrayB)
	printArr("Result", result)
}
