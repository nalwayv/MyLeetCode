package main

import (
	"fmt"
	"strings"
)

func mapWordWeights(words []string, weights []int) string {

	var result strings.Builder

	for _, word := range words {

		var sum int
		for _, ch := range word {
			// get ascii lowercase number between 0 and 25
			sum += weights[ch-'a']
		}

		sum %= 26

		// results are mapped to a reversed alphabet where z = 0 and a = 25
		// so we get the reversed index and convert it to a lowercase character
		at := rune(26-sum-1) + 'a'
		result.WriteString(string(at))
	}

	return result.String()
}

func main() {
	fmt.Println("3838. Weighted Word Mapping")

	words := []string{"abcd", "def", "xyz"}
	weights := []int{5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2}

	fmt.Printf("Result: %s\n", mapWordWeights(words, weights))
}
