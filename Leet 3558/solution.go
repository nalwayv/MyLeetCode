package main

import (
	"fmt"
	"math/big"
)

func maxDepth(tree map[int][]int, root int) int {
	children, ok := tree[root]
	if !ok {
		return 0
	}

	var depth int
	for _, child := range children {
		depth = max(depth, maxDepth(tree, child)+1)
	}

	return depth
}

func buildTree(edges [][]int) (map[int][]int, int) {
	tree := make(map[int][]int)
	seen := make(map[int]bool)
	var root int

	for _, edge := range edges {
		if len(edge) != 2 {
			continue
		}

		parent, child := edge[0], edge[1]

		if !seen[parent] {
			seen[parent] = true
			root += parent
		}

		if !seen[child] {
			seen[child] = true
			root += child
		}

		tree[parent] = append(tree[parent], child)
		root -= child
	}

	return tree, root
}

func AssignEdgeWeights(edges [][]int) int {
	tree, root := buildTree(edges)

	// big int version of 2 ** depth-1 % 1000000007
	var result big.Int
	result.Exp(
		big.NewInt(2),
		big.NewInt(int64(maxDepth(tree, root)-1)),
		big.NewInt(1000000007))

	return int(result.Uint64())
}

func main() {
	fmt.Println("3558. Number of Ways to Assign Edge Weights I")

	edges := [][]int{{1, 2}, {1, 3}, {3, 4}, {3, 5}}
	var result int = AssignEdgeWeights(edges)

	fmt.Printf("Result: %d\n", result)
}
