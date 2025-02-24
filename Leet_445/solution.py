class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def linked_list_to_int(self, head: ListNode|None) -> int:
        result: int = 0
        current: ListNode|None = head
        base: int = 10

        while current:
            result *= base
            result += current.val
            current = current.next
        
        return result
    
    def int_to_linked_list(self, num: int) -> ListNode|None:
        if num == 0:
            return ListNode(0)

        head: ListNode|None = None
        base: int = 10

        while num > 0:
            div, mod = divmod(num, base)
            if not head:
                head = ListNode(mod)
            else:
                tmp: ListNode|None = head
                head = ListNode(mod)
                head.next = tmp
            num = div

        return head

    def addTwoNumbers(self, l1: ListNode|None, l2: ListNode|None) -> ListNode|None:
        numA: int = self.linked_list_to_int(l1)
        numB: int = self.linked_list_to_int(l2)
        print(numA, numB)
        return self.int_to_linked_list(numA + numB)


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS


def print_list(head: ListNode|None) -> None:
    current: ListNode|None = head
    while current:
        print(f"{current.val}",end="")
        if current.next != None:
            print("->",end="")
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
# MAIN 


def main() -> None:
    print("445. Add Two Numbers II")
    
    headA: ListNode|None = create_list([7,2,4,3])
    headB: ListNode|None = create_list([5,6,4])

    sol = Solution()
    result: ListNode|None = sol.addTwoNumbers(headA, headB)
    print_list(result)


if __name__ == "__main__":
    main()