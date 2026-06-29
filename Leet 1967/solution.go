package main

import "fmt"

func containsSubString(word, substr string) bool {
	length := len(word) - len(substr) + 1

	for i := range length {
		if word[i:i+len(substr)] == substr {
			return true
		}
	}

	return false
}

func numOfStrings(patterns []string, word string) int {
	var count int

	for i := range patterns {
		if containsSubString(word, patterns[i]) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println("1967. Number of Strings That Appear as Substrings in Word")
	var count int = numOfStrings([]string{"a", "abc", "bc", "d"}, "abc")
	fmt.Printf("Result: %d\n", count)
}
