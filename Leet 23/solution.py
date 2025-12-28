class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def list_to_listnode(self, values: list[int]):
        head: ListNode|None = None
        tail: ListNode|None = None

        for val in values:
            if head == None:
                head = ListNode(val)
                tail = head
            elif tail:
                tail.next = ListNode(val)
                tail = tail.next

        return head

    def mergeKLists(self, lists: list[ListNode|None]) -> ListNode|None:
        if not lists:
            return None

        values: list[int] = []
        for current in lists:
            while current:
                values.append(current.val)
                current = current.next
        values.sort()

        return self.list_to_listnode(values)


def main() -> None:
    print('23. Merge k Sorted Lists')

    solution = Solution()

    case1 = [
        solution.list_to_listnode([1,4,5]),
        solution.list_to_listnode([1,3,4]),
        solution.list_to_listnode([2,6]),
    ]
    result = solution.mergeKLists(case1)
    while result:
        print(result.val)
        result = result.next


if __name__ == '__main__':
    main()