class ListNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.next: ListNode|None = None

    def __repr__(self) -> str:
        return f"ListNode( {self.val} )"


class Solution:
    def mergeInBetween(self, list1: ListNode|None, a: int, b: int, list2: ListNode|None) -> ListNode|None:
        if not list1 or not list2:
            return None

        # get list1 start node
        i: int = a
        l1_start: ListNode|None = None
        l1_end: ListNode|None = list1
        while i != 0 and l1_end:
            l1_start = l1_end
            l1_end = l1_end.next
            i -= 1

        # move to list1 end node
        j: int = b - a
        while j != 0 and l1_end:
            l1_end = l1_end.next
            j -= 1

        # get start and end of list2
        l2_start: ListNode|None = list2
        l2_end: ListNode|None = list2
        while l2_end and l2_end.next:
            l2_end = l2_end.next

        # connect
        if l1_start and l1_end:
            l1_start.next = l2_start
            l2_end.next = l1_end.next

        return list1


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
        return

    print("[",end="")
    current: ListNode|None = head
    while current:
        print(f"{current.val}",end="")
        if current.next != None:
            print(",",end="")
        current = current.next
    print("]")


def case_1(sol: Solution) -> None:
    print("CASE 1")

    nums_1: list[int] = [10,1,13,6,9,5]
    list_1 = create_linked_list(nums_1)

    nums_2: list[int] = [1000000,1000001,1000002]
    list_2 = create_linked_list(nums_2)
    
    a: int = 3
    b: int = 4

    result = sol.mergeInBetween(list_1, a, b, list_2)
    print_linked_list(result)


def case_2(sol: Solution) -> None:
    print("CASE 2")

    nums_1: list[int] = [0,1,2,3,4,5,6]
    list_1 = create_linked_list(nums_1)

    nums_2: list[int] = [1000000,1000001,1000002,1000003,1000004]
    list_2 = create_linked_list(nums_2)
    
    a: int = 2
    b: int = 5

    result = sol.mergeInBetween(list_1, a, b, list_2)
    print_linked_list(result)


def main() -> None:
    print("1669. Merge In Between Linked Lists")
    sol = Solution()
    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()
        