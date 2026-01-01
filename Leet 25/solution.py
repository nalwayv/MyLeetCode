class ListNode:
    def __init__(self, val: int=0):
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def list_to_listnode(self, values: list[int]) -> ListNode|None:
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

    def reverseKGroup(self, head: ListNode|None, k: int) -> ListNode|None:
        if not head:
            return None
        
        values: list[int] = []
        curr: ListNode|None = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        n: int = len(values)
        for i in range(0, n, k):
            if i + k <= n:
                for j, v in enumerate(reversed(values[i:i+k])):
                    values[i + j] = v

        return self.list_to_listnode(values)


def print_listnode(head: ListNode|None) -> None:
    if not head:
        return
    
    current = head
    print('[', end='')
    while current:
        print(f' {current.val} ', end='')
        current = current.next
    print(']')


def test_case(solution: Solution, nums: list[int], k: int) -> None:
    head = solution.list_to_listnode(nums)
    head = solution.reverseKGroup(head, k)
    print_listnode(head)


def main() -> None:
    print('25. Reverse Nodes in k-Group')

    solution = Solution()

    test_case(solution, [1,2,3,4,5], 2)
    test_case(solution, [1,2,3,4,5], 3)
    test_case(solution, [1,2], 2)


if __name__ == '__main__':
    main()