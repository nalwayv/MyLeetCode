package main

import (
	"fmt"
	"strings"
)

// encoding for count and say
func encode(s string) string {
	var result strings.Builder

	p1 := 0
	for p2 := 0; p2 < len(s); p2++ {
		if s[p1] != s[p2] {
			fmt.Fprintf(&result, "%d%c", p2-p1, s[p1])
			p1 = p2
		}
	}

	if len(s)-p1 > 0 {
		fmt.Fprintf(&result, "%d%c", len(s)-p1, s[p1])
	}

	return result.String()
}

func countAndSay(n int) string {
	result := "1"
	for i := 0; i < n-1; i++ {
		// use result as next input
		result = encode(result)
	}
	return result
}

func main() {
	fmt.Println("38. Count and Say")

	var result string = countAndSay(4)
	fmt.Println(result)
}
