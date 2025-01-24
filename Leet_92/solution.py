class ListNode:
    def __init__(self, val: int=0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def _move_to_node(self, head: ListNode|None, index: int) -> ListNode|None:
        curr:ListNode|None = head
        while index != 0 and curr:
            curr = curr.next
            index -= 1
        return curr
    
    def _swap_node_values(self, a: ListNode|None, b: ListNode|None) -> None:
        if not a or not b:
            return
        a.val, b.val = b.val, a.val

    def reverseBetween(self, head: ListNode|None, left: int, right: int) -> ListNode|None:
        if not head:
            return None
        
        curr: ListNode|None = self._move_to_node(head, left-1)
        diff: int = (right - left) + 1
        nodes: list[ListNode|None] = []
        while diff > 0 and curr:
            nodes.append(curr)
            curr = curr.next
            diff -= 1

        if nodes:
            lo: int = 0
            hi: int = len(nodes) - 1
            while lo < hi:
                self._swap_node_values(nodes[lo], nodes[hi])
                lo += 1
                hi -= 1

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

    current: ListNode|None = head
    while current:
        print(f"{current.val}",end="")
        if current.next != None:
            print("->",end="")
        current = current.next
    print("")


def main() -> None:
    print("92. Reverse Linked List II")

    sol = Solution()
    
    nums: list[int] = [1,2,3,4,5]
    head: ListNode|None = create_linked_list(nums)
    
    left: int = 1
    right: int = 5
    head = sol.reverseBetween(head, left, right)

    print_linked_list(head)


if __name__ == "__main__":
    main()