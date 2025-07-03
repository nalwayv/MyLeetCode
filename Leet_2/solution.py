# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int):
        self.val:int = val
        self.next:ListNode|None = None


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. 

    The digits are stored in reverse order, and each of their nodes contains a single digit. 

    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    
    Example:

        Input: A = [2,4,3], B = [5,6,4]

        Output: [7,0,8]

        Explanation: 342 + 465 = 807.

    Note:

        number in list should be within range 0-9
    """
    def build_int(self, head: ListNode|None, ref: list[int]):
        if not head:
            return
        
        self.build_int(head.next, ref)

        ref[0] *= 10
        ref[0] += head.val

    def addTwoNumbers(self, l1: ListNode|None, l2: ListNode|None) -> ListNode|None:
        num_1: list[int] = [0]
        self.build_int(l1, num_1)

        num_2: list[int] = [0]
        self.build_int(l2, num_2)

        result: int = num_1[0] + num_2[0]
        if result == 0:
            return ListNode(0)

        head: ListNode|None = None
        tail: ListNode|None = None
        while result:
            if not head:
                head = ListNode(result % 10)
                tail = head
            elif tail:
                tail.next = ListNode(result % 10)
                tail = tail.next
            result //= 10

        return head


def main() -> None:
    print("2. Add Two Numbers")

    head_1 = ListNode(2)
    head_1.next = ListNode(4)
    head_1.next.next = ListNode(3)

    head_2 = ListNode(5)
    head_2.next = ListNode(6)
    head_2.next.next = ListNode(4)

    sol = Solution()
    current: ListNode|None = sol.addTwoNumbers(head_1, head_2)
    while current:
        print(current.val)
        current = current.next


if __name__ == "__main__":
    main()