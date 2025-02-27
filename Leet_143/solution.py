class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def reorderList(self, head: ListNode|None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # You are given the head of a singly linked-list. The list can be represented as:
        # L0 → L1 → … → Ln - 1 → Ln
        # Reorder the list to be on the following form:
        # L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

        # store nodes to help with pointer swaping
        nodes: list[ListNode] = []
        current: ListNode|None = head
        while current:
            nodes.append(current)
            current = current.next

        # swap pointers
        lo: int = 0
        hi: int = len(nodes)-1
        pick_low: bool = True

        while lo < hi:
            if pick_low:
                nodes[lo].next = nodes[hi]
                lo += 1
                pick_low = False
            else:
                nodes[hi].next = nodes[lo]
                hi -= 1
                pick_low = True

        # make hi the new end
        nodes[hi].next = None


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS


def print_list(head: ListNode|None) -> None:
    current: ListNode|None = head
    
    while current:
        print(f"{current.val}", end="")
        if current.next != None:
            print("->", end="")
        current = current.next

    print("")


def create_list(nums: list[int]) -> ListNode|None:
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


# -----------------------------------------------------------------------------
# TEST CASES


def case_1(sol: Solution) -> None:
    print("Case 1: [1,2,3,4] --> [1,4,2,3]")
    head: ListNode|None = create_list([1,2,3,4])

    sol = Solution()
    sol.reorderList(head)
    print_list(head)


def case_2(sol: Solution) -> None:
    print("Case 2: [1,2,3,4,5] --> [1,5,2,4,3]")
    head: ListNode|None = create_list([1,2,3,4,5])

    sol = Solution()
    sol.reorderList(head)
    print_list(head)


def case_3(sol: Solution) -> None:
    print("Case 3: [1,2] --> [1,2]")
    head: ListNode|None = create_list([1,2])

    sol = Solution()
    sol.reorderList(head)
    print_list(head)


def case_4(sol: Solution) -> None:
    print("Case 4: [1] --> [1]")
    head: ListNode|None = create_list([1])

    sol = Solution()
    sol.reorderList(head)
    print_list(head)


# -----------------------------------------------------------------------------
# MAIN 


def main() -> None:
    print("143. Reorder List")

    sol = Solution()
    
    case_1(sol)
    case_2(sol)
    case_3(sol)
    case_4(sol)


if __name__ == "__main__":
    main()