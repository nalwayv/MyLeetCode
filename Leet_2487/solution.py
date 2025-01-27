# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def reverse(self, head: ListNode|None) -> ListNode|None:
        curr: ListNode|None = head
        prev: ListNode|None = None
        nxt: ListNode|None = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def removeNodes(self, head: ListNode|None) -> ListNode|None:
        if not head:
            return head
        
        head = self.reverse(head)
        if not head: 
            return head

        max_value: int = head.val
        new_head = ListNode(max_value)
        curr = head.next
        
        while curr:
            if max_value <= curr.val:
                # new head
                node = ListNode(curr.val)
                node.next = new_head
                new_head = node
                max_value = curr.val

            curr = curr.next

        return new_head


def create_linked_list(nums: list[int]) -> ListNode|None:
    head: ListNode|None = None
    tail: ListNode|None = None
    for num in nums:
        if not head:
            head = ListNode(num)
            tail = head
        elif tail:
            tail.next = ListNode(num)
            tail = tail.next
    return head


def print_linked_list(head: ListNode|None) -> None:
    if head == None:
        print("None")


    current: ListNode|None = head
    print("[",end="")
    while current:
        print(f"{current.val}",end="")
        if current.next != None:
            print(", ",end="")
        current = current.next
    print("]")


def case_1(sol: Solution) -> None:
    print("Case 1")
    nums: list[int] = [5,2,13,3,8]
    head: ListNode|None = create_linked_list(nums)
    
    head = sol.removeNodes(head)
    print_linked_list(head)


def case_2(sol: Solution) -> None:
    print("Case 2")
    nums: list[int] = [1,1,1,1]
    head: ListNode|None = create_linked_list(nums)
    
    head = sol.removeNodes(head)
    print_linked_list(head)


def main() -> None:
    print("2487. Remove Nodes From Linked List")
    sol = Solution()

    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()