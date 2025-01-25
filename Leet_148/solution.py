class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def _get_list_values(self, head: ListNode|None) -> list[int]:
        values: list[int] = []
        curr: ListNode|None = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

    def _change_list_values(self, head: ListNode|None, values: list[int]) -> None:
        idx:int = 0
        n: int = len(values)
        curr: ListNode|None = head
        while idx < n and curr:
            curr.val = values[idx]
            curr = curr.next
            idx += 1

    def sortList(self, head: ListNode|None) -> ListNode|None:
        values: list[int] = self._get_list_values(head)
        values.sort()
        self._change_list_values(head, values)
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


def case_1(sol: Solution) -> None:
    print("Case 1")
    nums = [4,2,1,3]
    head = create_linked_list(nums)
    print_linked_list(head)
    head = sol.sortList(head)
    print_linked_list(head)


def case_2(sol: Solution) -> None:
    print("Case 2")
    nums = [-1,5,3,4,0]
    head = create_linked_list(nums)
    print_linked_list(head)
    head = sol.sortList(head)
    print_linked_list(head)


def main() -> None:
    print("148. Sort List")
    sol = Solution()

    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()