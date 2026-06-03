package main

import (
	"fmt"
	"math"
)

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	var result int = math.MaxInt
	var water int = math.MaxInt
	var land int = math.MaxInt

	// land then water
	for i, start := range landStartTime {
		land = min(land, start+landDuration[i])
	}

	for i, start := range waterStartTime {
		result = min(result, max(land, start)+waterDuration[i])
	}

	// water then land
	for i, start := range waterStartTime {
		water = min(water, start+waterDuration[i])
	}

	for i, start := range landStartTime {
		result = min(result, max(water, start)+landDuration[i])
	}

	return result
}

func main() {
	fmt.Println("3635. Earliest Finish Time for Land and Water Rides II")
	landStartTime := []int{2, 8}
	landDuration := []int{4, 1}
	waterStartTime := []int{6}
	waterDuration := []int{3}

	var result int = earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
	fmt.Printf("Earlest Finish Time = %d\n", result)
}
