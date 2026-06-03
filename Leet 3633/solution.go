package main

import (
	"fmt"
	"math"
)

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	var landLen int = min(len(landStartTime), len(landDuration))
	var waterLen int = min(len(waterStartTime), len(waterDuration))

	// starting with land ride then water
	var land int = math.MaxInt
	for i := range landLen {
		end := landStartTime[i] + landDuration[i]
		for j := range waterLen {
			startTime := waterStartTime[j]
			duration := waterDuration[j]

			land = min(land, max(end, startTime)+duration)
		}
	}

	// starting with water ride then land
	var water int = math.MaxInt
	for i := range waterLen {
		end := waterStartTime[i] + waterDuration[i]
		for j := range landLen {
			startTime := landStartTime[j]
			duration := landDuration[j]

			water = min(water, max(end, startTime)+duration)
		}
	}

	return min(land, water)
}

func main() {
	fmt.Println("3633. Earliest Finish Time for Land and Water Rides I")
	landStartTime := []int{2, 8}
	landDuration := []int{4, 1}
	waterStartTime := []int{6}
	waterDuration := []int{3}

	var finishTime int = earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
	fmt.Printf("Earliest Finish Time = %d\n", finishTime)
}
