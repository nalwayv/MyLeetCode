class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def partition(self, head: ListNode|None, x: int) -> ListNode|None:
        # partition

        less: list[int] = []
        more: list[int] = []
        current: ListNode|None = head
        while current:
            if current.val < x:
                less.append(current.val)
            else:
                more.append(current.val)
            current = current.next

        # build new linked list

        result_head: ListNode|None = None
        result_tail: ListNode|None = None

        for num in less:
            if not result_head:
                result_head = ListNode(num)
                result_tail = result_head
            elif result_tail:
                result_tail.next = ListNode(num)
                result_tail = result_tail.next

        for num in more:
            if not result_head:
                result_head = ListNode(num)
                result_tail = result_head
            elif result_tail:
                result_tail.next = ListNode(num)
                result_tail = result_tail.next

        return result_head


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
    print("Case 1")
    head: ListNode|None = create_list([1,4,3,2,5,2])
    x: int = 3
    result: ListNode|None = sol.partition(head, x)
    print_list(result)


def case_2(sol: Solution) -> None:
    print("Case 2")
    head: ListNode|None = create_list([2,1])
    x: int = 2
    result: ListNode|None = sol.partition(head, x)
    print_list(result)


def case_3(sol: Solution) -> None:
    print("Case 3")
    head: ListNode|None = create_list([1,3,4,3,1,1,5,2,2])
    x: int = 4
    result: ListNode|None = sol.partition(head, x)
    print_list(result)


# -----------------------------------------------------------------------------
# MAIN 


def main() -> None:
    print("86. Partition List")

    sol = Solution()
    case_1(sol)
    case_2(sol)
    case_3(sol)


if __name__ == "__main__":
    main()