package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func newNode(value int) *ListNode {
	node := new(ListNode)
	node.Val = value
	return node
}

func toSlice(head *ListNode) []*ListNode {
	var nodes []*ListNode
	for current := head; current != nil; current = current.Next {
		nodes = append(nodes, current)
	}
	return nodes
}

func pairSum(head *ListNode) int {
	nodes := toSlice(head)

	maxPair := -1
	p1 := 0
	p2 := len(nodes) - 1

	for p1 < p2 {
		var val1 = nodes[p1].Val
		var val2 = nodes[p2].Val

		fmt.Printf("%d - %d\n", val1, val2)

		maxPair = max(maxPair, val1+val2)

		p1++
		p2--
	}

	return maxPair
}

func newList(nums []int) *ListNode {
	var head *ListNode = new(ListNode)
	head.Val = nums[0]

	var tail *ListNode = head

	for i := 1; i < len(nums); i++ {
		tail.Next = newNode(nums[i])
		tail = tail.Next
	}

	return head
}

func printListNode(head *ListNode) {
	for current := head; current != nil; current = current.Next {
		fmt.Println(current.Val)
	}
}

func main() {
	fmt.Println("2130. Maximum Twin Sum of a Linked List")

	nums := []int{4, 2, 2, 3}
	var head *ListNode = newList(nums)
	printListNode(head)

	fmt.Printf("Result: %d\n", pairSum(head))
}
