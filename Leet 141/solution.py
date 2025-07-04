class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: ListNode|None = None


class Solution:
    def hasCycle(self, head: ListNode|None) -> bool:
        if head == None or head.next == None:
            return False
        
        slow: ListNode|None = head
        fast: ListNode|None = head.next
            
        while fast != None and fast.next != None:
            if fast == slow:
                return True
            
            fast = fast.next.next
            if slow:
                slow = slow.next
            
        return False


def build_linked_list(nums: list[int]) -> ListNode:
    """Build linked list from array
    """
    n: int = len(nums)
    head = ListNode(nums[0])
    tail = head
    for i in range(1, n):
        #set tail
        tail.next = ListNode(nums[i])
        #move to new endpoint
        tail = tail.next
    return head


def move_to_node(head: ListNode|None, to: int) -> ListNode|None:
    """Move from head to node at index using a zero based index
    """
    while to != 0 and head:
        head = head.next
        to -= 1
    return head


def connect_nodes(head: ListNode|None, idx1: int, idx2: int):
    """Create a connection between nodes at index's if found
    """
    a: ListNode|None = move_to_node(head, idx1)
    b: ListNode|None = move_to_node(head, idx2)
    if a and b:
        a.next = b


def main() -> None:
    head: ListNode = build_linked_list([3, 2, 0, -4])

    # create cycle
    connect_nodes(head, 3, 1)

    sol = Solution()
    print(sol.hasCycle(head))


if __name__ == "__main__":
    main()