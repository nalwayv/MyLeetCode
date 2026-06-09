package main

import "fmt"

func all(arr []bool) bool {
	for _, v := range arr {
		if !v {
			return false
		}
	}
	return true
}

func canVisitAllRooms(rooms [][]int) bool {
	var keys []int
	visited := make([]bool, len(rooms))
	// there is no room zero as keys only go from  1..n
	visited[0] = true

	// add all keys from first room
	for _, key := range rooms[0] {
		keys = append(keys, key)
	}

	for len(keys) > 0 {
		key := keys[len(keys)-1]
		keys = keys[:len(keys)-1]

		if visited[key] {
			continue
		}

		visited[key] = true

		for _, key := range rooms[key] {
			keys = append(keys, key)
		}

	}

	return all(visited)
}

func main() {
	fmt.Println("841. Keys and Rooms")

	rooms := [][]int{{1}, {2}, {3}, {}}
	var result bool = canVisitAllRooms(rooms)
	if result {
		fmt.Println("Can visit all rooms: yes")
	} else {
		fmt.Println("Can visit all rooms: no")
	}
}
