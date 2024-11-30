class ListNode:
    def __init__(self, value: int = 0) -> None:
        self.value: int = value
        self.next: ListNode|None = None


class Solution:
    @staticmethod
    def _swap(a: ListNode|None, b: ListNode|None) -> None:
        if not a or not b:
            return
        a.value, b.value = b.value, a.value

    def deleteNode(self, node: ListNode|None) -> None:
        """Delete node from Linked List without being given its head.\n
        
        All the values of the linked list are unique,\n 
        and it is guaranteed that the given node `node` is not\n
        the last node in the linked list.

        Args:
            node (ListNode): A node from a `linked list`.

        Returns:
            None just alters `linked list` that node is connected to.
        """
        prev: ListNode|None = None
        curr: ListNode|None = node

        # move current to prev from end
        while curr and curr.next:
            if prev:
                Solution._swap(prev, curr)
            prev = curr
            curr = curr.next

        # final swap and remove end
        if prev and curr:
            Solution._swap(prev, curr)
            prev.next = None


def _create_listnode(nums: list[int]) -> ListNode|None:
    """`HELPER FUNCTION`\n
    Create a linked list from a list of ints.

    Args:
        nums (list[int]): convert to linked list.

    Returns:
        Linked list `head` node.
    """
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


def _move_to(head: ListNode|None, index: int) -> ListNode|None:
    """`HELPER FUNCTION`\n
    Move to index and return current node from linked list.

    Args:
        node (ListNode): Head of a linked list `linked list`.

    Returns:
        `node` from Linked list or None.
    """
    curr:ListNode|None = head
    while index !=  0 and curr:
        curr = curr.next
        index -= 1
    return curr


def _print_linked_list(head: ListNode|None) -> None:
    """`HELPER FUNCTION`\n
    Print linked list to console
    """
    curr:ListNode|None = head
    print("", end="")
    while curr:
        if not curr.next:
            print(f"{curr.value}", end="")
        else:
            print(f"{curr.value}->", end="")
        curr = curr.next
    print("")


def case1(sol: Solution) -> None:
    print("CASE 1:")
    print("  Remove 5 from  4->5->1->9")

    nums: list[int] = [4, 5, 1, 9]
    head: ListNode|None = _create_listnode(nums)
    print("  Before: ",end="")
    _print_linked_list(head)

    curr: ListNode|None = _move_to(head, 1)
    if curr:
        sol.deleteNode(curr)
        print("  After: ",end="")
        _print_linked_list(head)

    print("")


def case2(sol: Solution) -> None:
    print("CASE 2:")
    print("  Remove 1 from  4->5->1->9")
    
    nums: list[int] = [4, 5, 1, 9]
    head: ListNode|None = _create_listnode(nums)
    print("  Before: ",end="")
    _print_linked_list(head)

    curr: ListNode|None = _move_to(head, 2)
    if curr:
        sol.deleteNode(curr)
        print("  After: ",end="")
        _print_linked_list(head)

    print("")


def main() -> None:
    print("237. Delete Node in a Linked List")
    
    sol = Solution()
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()