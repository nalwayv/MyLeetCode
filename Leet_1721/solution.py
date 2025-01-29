# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def _length(self, head: ListNode|None) -> int:
        curr: ListNode|None = head
        length: int = 0
        while curr:
            curr = curr.next
            length += 1
        return length

    def _get_node_at(self, head: ListNode|None, idx: int) -> ListNode|None:
        curr: ListNode|None = head
        while idx != 0 and curr:
            idx -= 1
            curr = curr.next
        return curr

    def swapNodes(self, head: ListNode|None, k: int) -> ListNode|None:
        if not head:
            return None

        if k < 1:
            return head

        length: int = self._length(head)
        nodeA: ListNode|None = self._get_node_at(head, k - 1)    
        nodeB: ListNode|None = self._get_node_at(head, length - k)

        if nodeA and nodeB:
            nodeA.val, nodeB.val = nodeB.val, nodeA.val

        return head


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

    print("[",end="")
    current: ListNode|None = head
    while current:
        print(f"{current.val}",end="")
        if current.next != None:
            print(",",end="")
        current = current.next
    print("]")


def case_1(sol: Solution) -> None:
    print("Case 1")

    nums: list[int] = [1,2,3,4,5]
    k: int = 2
    head: ListNode|None = create_linked_list(nums)

    print(f"Before swap k={k}")
    print_linked_list(head)

    head = sol.swapNodes(head, k)
    print(f"After swap k={k}")
    print_linked_list(head)
    print("")


def case_2(sol: Solution) -> None:
    print("Case 2")

    nums: list[int] = [7,9,6,6,7,8,3,0,9,5]
    k: int = 5
    head: ListNode|None = create_linked_list(nums)

    print(f"Before swap k={k}")
    print_linked_list(head)
    
    head = sol.swapNodes(head, k)
    print(f"After swap k={k}")
    print_linked_list(head)
    print("")


def case_3(sol: Solution) -> None:
    print("Case 3")

    nums: list[int] = [1,2]
    k: int = 1
    head: ListNode|None = create_linked_list(nums)

    print(f"Before swap k={k}")
    print_linked_list(head)
    
    head = sol.swapNodes(head, k)
    print(f"After swap k={k}")
    print_linked_list(head)
    print("")


def main() -> None:
    print("1721. Swapping Nodes in a Linked List")
    
    sol = Solution()
    
    case_1(sol)
    case_2(sol)
    case_3(sol)


if __name__ == "__main__":
    main()