class ListNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def mergeNodes(self, head: ListNode|None) -> ListNode|None:    
        if not head:
            return None
        
        new_head: ListNode|None = None
        new_tail: ListNode|None = None
        
        prev: ListNode|None = head
        curr: ListNode|None = head.next
        current_total: int = 0

        while prev and curr:
            
            if curr.val != 0:
                current_total += prev.val
            else:
                val: int = current_total + prev.val
                current_total = 0
    
                if not new_head:
                    new_head = ListNode(val)
                    new_tail = new_head
                elif new_tail:
                    new_tail.next = ListNode(val)
                    new_tail = new_tail.next
            
            prev = prev.next    
            curr = curr.next

        return new_head


def create_linked_list(values: list[int]) -> ListNode|None:
    head: ListNode|None = None
    tail: ListNode|None = None
    for num in values:
        if not head:
            head = ListNode(num)
            tail = head
        elif tail:
            tail.next = ListNode(num)
            tail = tail.next
    return head


# HELPER FUNCTION


def print_linked_list(head: ListNode|None, msg: str = "") -> None:
    if not head:
        return
    
    print(f"{msg}[", end="")
    current = head
    while current:
        print(f" {current.val} ", end="")
        current = current.next
    print("]")


# TEST CASES


def test_case_1(sol: Solution) -> None:
    head = create_linked_list([0,3,1,0,4,5,2,0])
    head_2 = sol.mergeNodes(head)
    print_linked_list(head_2)


def test_case_2(sol: Solution) -> None:
    head = create_linked_list([0,1,0,3,0,2,2,0])
    head_2 = sol.mergeNodes(head)
    print_linked_list(head_2)


# MAIN


def main() -> None:
    print("2181. Merge Nodes in Between Zeros")

    sol = Solution()
    test_case_1(sol)
    test_case_2(sol)


if __name__ == "__main__":
    main()