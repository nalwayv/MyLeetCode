package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func newNode(value int) *ListNode {
	node := new(ListNode)
	node.Val = value
	return node
}

func deleteMiddle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}

	mid := head
	prev := head
	length := 1
	for curr := head; curr.Next != nil; curr = curr.Next {
		length++

		if length%2 == 0 {
			prev = mid
			mid = mid.Next
		}
	}
	prev.Next = mid.Next
	mid = nil

	return head
}

func createList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}

	head := newNode(nums[0])
	tail := head
	for i := 1; i < len(nums); i++ {
		tail.Next = newNode(nums[i])
		tail = tail.Next
	}
	return head
}

func printList(head *ListNode) {
	fmt.Print("[")
	for current := head; current != nil; current = current.Next {
		fmt.Printf(" %d ", current.Val)
	}
	fmt.Println("]")
}

func main() {
	fmt.Println("2095. Delete the Middle Node of a Linked List")
	var head *ListNode = createList([]int{1, 3, 4, 7, 1, 2, 6})

	fmt.Println("Before:")
	printList(head)

	fmt.Println("After:")
	head = deleteMiddle(head)
	printList(head)
}
