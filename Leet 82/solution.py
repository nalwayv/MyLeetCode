class ListNode:
    def __init__(self, val: int=0):
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    @staticmethod
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

    @staticmethod
    def print_linked_list(head: ListNode|None) -> None:
        if not head:
            return
        
        print("[", end="")
        current = head
        while current:
            print(f" {current.val} ", end="")
            current = current.next
        print("]")

    def deleteDuplicates(self, head: ListNode|None) -> ListNode|None:
        if not head:
            return head
        
        TARGET: int = 1
        values: list[int] = []

        curr: ListNode|None = head
        while curr:
            other = curr
            count: int = 0
            while other and other.val == curr.val:
                other = other.next
                count += 1

            if count == TARGET:
                values.append(curr.val)

            curr = other

        return Solution.create_linked_list(values)


def case1(sol: Solution) -> None:
    print("Case 1")
    numbers = [1,2,3,3,4,4,5]
    head = Solution.create_linked_list(numbers)
    # -> [1,2,5] as 3,4 appears more then once
    result = sol.deleteDuplicates(head)
    Solution.print_linked_list(result)


def case2(sol: Solution) -> None:
    print("Case 2")
    numbers = [1,1,1,2,3]
    head = Solution.create_linked_list(numbers)
    # -> [2,3] as 1 appears more then ones
    result = sol.deleteDuplicates(head)
    Solution.print_linked_list(result)


def case3(sol: Solution) -> None:
    print("Case 3")
    numbers = [-3,-2,-2,-1,0,1,2,2,3]
    head = Solution.create_linked_list(numbers)
    result = sol.deleteDuplicates(head)
    Solution.print_linked_list(result)


def main() -> None:
    print("82. Remove Duplicates from Sorted List II")

    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()