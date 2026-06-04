package main

import (
	"fmt"
	"strconv"
)

func totalWaviness(num1, num2 int) int {
	var result int = 0

	for i := num1; i <= num2; i++ {
		var num string = strconv.Itoa(i)

		if len(num) < 3 {
			continue
		}

		var count int = 0
		for j := 0; j <= len(num)-3; j++ {
			current := num[j : j+3]
			lo := current[0]
			mid := current[1]
			hi := current[2]

			if (mid > lo && mid > hi) || (mid < lo && mid < hi) {
				count++
			}
		}

		result += count
	}

	return result
}

func main() {
	fmt.Println("3751. Total Waviness of Numbers in Range I")

	var waviness int = totalWaviness(120, 130)
	fmt.Printf("Waviness between 120 and 130 is %d\n", waviness)
}
