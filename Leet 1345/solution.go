package main

import "fmt"

type Node struct {
	Index    int
	Distance int
}

type Queue []Node

func (queue *Queue) Size() int {
	return len(*queue)
}

func (queue *Queue) Enqueue(node Node) {
	*queue = append(*queue, node)
}

func (queue *Queue) Dequeue() (Node, error) {
	if queue.Size() == 0 {
		return Node{}, fmt.Errorf("Queue: queue is empty")
	}

	node := (*queue)[0]
	*queue = (*queue)[1:]
	return node, nil
}

func minJumps(arr []int) int {
	graph := make(map[int][]int)

	for idx, val := range arr {
		graph[val] = append(graph[val], idx)
	}

	que := &Queue{}
	que.Enqueue(Node{
		Index:    0,
		Distance: 0,
	})

	visited := make(map[int]bool)

	for que.Size() > 0 {
		current, _ := que.Dequeue()

		if visited[current.Index] {
			continue
		}

		visited[current.Index] = true

		if current.Index == len(arr)-1 {
			return current.Distance
		}

		graph[arr[current.Index]] = append(graph[arr[current.Index]], current.Index+1)
		graph[arr[current.Index]] = append(graph[arr[current.Index]], current.Index-1)

		for i := range graph[arr[current.Index]] {
			var neighbour int = graph[arr[current.Index]][i]

			if 0 <= neighbour && neighbour < len(arr) {
				que.Enqueue(Node{
					Index:    neighbour,
					Distance: current.Distance + 1,
				})
			}
		}

		graph[arr[current.Index]] = nil
	}

	return -1
}

func main() {
	fmt.Println("1345. Jump Game IV")

	var arr []int = []int{100, -23, -23, 404, 100, 23, 23, 23, 3, 404}
	var jumps int = minJumps(arr)
	fmt.Printf("Min Jumps: %d\n", jumps)
}
