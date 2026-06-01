package main

import (
	"fmt"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Queue using two stacks
type Queue struct {
	stackA []*TreeNode
	stackB []*TreeNode
}

func (q *Queue) Enqueue(node *TreeNode) {
	q.stackA = append(q.stackA, node)
}

func (q *Queue) Dequeue() *TreeNode {
	// move values from a to b
	if len(q.stackB) == 0 {
		for len(q.stackA) > 0 {
			var current *TreeNode = q.stackA[len(q.stackA)-1]
			q.stackA = q.stackA[:len(q.stackA)-1]

			q.stackB = append(q.stackB, current)
		}
	}

	// pop result
	item := q.stackB[len(q.stackB)-1]
	q.stackB = q.stackB[:len(q.stackB)-1]

	return item
}

func (q *Queue) IsEmpty() bool {
	return len(q.stackA) == 0 && len(q.stackB) == 0
}

func (q *Queue) Count() int {
	return len(q.stackA) + len(q.stackB)
}

func CodecSerialize(root *TreeNode) string {
	if root == nil {
		return ""
	}

	que := Queue{}
	que.Enqueue(root)

	var sb strings.Builder
	sb.WriteString(strconv.Itoa(root.Val))

	for !que.IsEmpty() {
		count := que.Count()

		for count > 0 {
			count--

			current := que.Dequeue()

			sb.WriteString(",")
			if current.Left != nil {
				que.Enqueue(current.Left)
				sb.WriteString(strconv.Itoa(current.Left.Val))
			} else {
				sb.WriteString("null")
			}

			sb.WriteString(",")
			if current.Right != nil {
				que.Enqueue(current.Right)
				sb.WriteString(strconv.Itoa(current.Right.Val))
			} else {
				sb.WriteString("null")
			}
		}
	}

	var result string = sb.String()

	// trim repeating ",null" from the end of the result string
	var target string = ",null"
	var targetLen int = len(target)
	var resultEnd int = len(result)
	for resultEnd >= targetLen && result[resultEnd-targetLen:resultEnd] == target {
		resultEnd -= targetLen
	}

	return result[:resultEnd]
}

// helper function that trys to convert a value from values at idx to an int
//
// the []string values consists of numbers or null
func tryGetValue(values []string, idx int) (int, bool) {
	if idx < 0 || idx >= len(values) || values[idx] == "null" {
		return -1, false
	}

	val, err := strconv.Atoi(values[idx])
	if err != nil {
		return -1, false
	}

	return val, true
}

func CodecDeserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}

	var values []string = strings.Split(data, ",")
	idx := 0

	rootVal, ok := tryGetValue(values, idx)
	if !ok {
		return nil
	}

	root := new(TreeNode)
	root.Val = rootVal

	que := Queue{}
	que.Enqueue(root)
	idx += 1

	for que.Count() > 0 && idx < len(values) {
		current := que.Dequeue()

		leftVal, ok := tryGetValue(values, idx)
		if ok {
			current.Left = new(TreeNode)
			current.Left.Val = leftVal
			que.Enqueue(current.Left)
		}
		idx++

		rightVal, ok := tryGetValue(values, idx)
		if ok {
			current.Right = new(TreeNode)
			current.Right.Val = rightVal
			que.Enqueue(current.Right)
		}
		idx++
	}

	return root
}

func printTree(root *TreeNode) {
	if root == nil {
		return
	}

	fmt.Println(root.Val)
	printTree(root.Left)
	printTree(root.Right)
}

func createTree() *TreeNode {
	root := new(TreeNode)
	root.Val = 1

	root.Left = new(TreeNode)
	root.Left.Val = 2

	root.Right = new(TreeNode)
	root.Right.Val = 3

	root.Right.Left = new(TreeNode)
	root.Right.Left.Val = 4

	root.Right.Right = new(TreeNode)
	root.Right.Right.Val = 5
	return root
}

func main() {
	fmt.Println("297. Serialize and Deserialize Binary Tree")

	var root *TreeNode = createTree()

	var sRoot string = CodecSerialize(root)
	fmt.Println(sRoot)

	var dRoot *TreeNode = CodecDeserialize(sRoot)
	printTree(dRoot)
}
