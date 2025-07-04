class ListNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def getDecimalValue(self, head: ListNode|None) -> int:
        result: int = 0
        curr: ListNode|None = head
        while curr:
            result *= 2
            if curr.val == 1:
                result += 1
            curr = curr.next
        return result


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


def case_1(sol: Solution) -> None:
    nums: list[int] = [1,0,1]
    root: ListNode|None = create_linked_list(nums)
    result: int = sol.getDecimalValue(root)
    print(f"Case 1: {result} == 5")


def case_2(sol: Solution) -> None:
    nums: list[int] = [0]
    root: ListNode|None = create_linked_list(nums)
    result: int = sol.getDecimalValue(root)
    print(f"Case 2: {result} == 0")


def main() -> None:
    print("1290. Convert Binary Number in a Linked List to Integer")

    sol = Solution()

    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()
        