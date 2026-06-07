package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func newTreeNode(val int) *TreeNode {
	newNode := new(TreeNode)
	newNode.Val = val
	newNode.Left = nil
	newNode.Right = nil
	return newNode
}

func createBinaryTree(descriptions [][]int) *TreeNode {
	if len(descriptions) == 0 {
		return nil
	}

	tree := make(map[int]*TreeNode)
	root := 0

	for _, current := range descriptions {
		if len(current) != 3 {
			continue
		}

		parent := current[0]
		child := current[1]
		isLeft := current[2]

		// add parent to tree
		if _, ok := tree[parent]; !ok {
			tree[parent] = newTreeNode(parent)
			root += parent
		}

		// add child to tree
		if _, ok := tree[child]; !ok {
			tree[child] = newTreeNode(child)
			root += child
		}

		// set connection
		if isLeft == 1 {
			tree[parent].Left = tree[child]
		} else {
			tree[parent].Right = tree[child]
		}

		// by removing child values from sum you are left with only the root value
		root -= child

	}

	return tree[root]
}

func printTree(root *TreeNode) {
	if root == nil {
		return
	}

	fmt.Printf("Tree: %d\n", root.Val)

	printTree(root.Left)
	printTree(root.Right)
}

func main() {
	fmt.Println("2196. Create Binary Tree From Descriptions")
	descriptions := [][]int{
		{20, 15, 1},
		{20, 17, 0},
		{50, 20, 1},
		{50, 80, 0},
		{80, 19, 1}}

	var root *TreeNode = createBinaryTree(descriptions)

	printTree(root)
}
