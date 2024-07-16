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
    def concat_ints_reversed(self, l1: ListNode|None) -> int:
        stk:list[int] = []
        count: int = 0
        current: ListNode | None = l1
        while current:
            stk.append(current.val)
            current = current.next
            count += 1

        result: int = 0
        for i in reversed(range(count)):
            result *= 10
            result += stk[i]

        return result
    
    def deconstruct_int_to_list(self, num: int) -> ListNode|None:
        head: ListNode|None = None
        tail: ListNode|None = None
        
        while True:
            current: int = num % 10
            if not head:
                head = ListNode(current)
                tail = head
            elif tail:
                tail.next = ListNode(current)
                tail = tail.next

            num //= 10
            if num == 0:
                break
            
        return head

    def addTwoNumbers(self, l1: ListNode|None, l2: ListNode|None) -> ListNode|None:
        num1: int = self.concat_ints_reversed(l1)
        num2: int = self.concat_ints_reversed(l2)
        num3: int = num1 + num2
        return self.deconstruct_int_to_list(num3)
    
    def print_list(self, head: ListNode|None) -> None:
        current: ListNode|None = head
        while current:
            print(f"{current.val}")
            current = current.next

    def new_list_from_list(self, nums: list[int]) -> ListNode|None:
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


def main() -> None:
    solution = Solution()
    a: ListNode|None = solution.new_list_from_list([1,2,6])
    b: ListNode|None = solution.new_list_from_list([1,9,0])

    result: ListNode|None = solution.addTwoNumbers(a, b)
    solution.print_list(result)


if __name__ == "__main__":
    main()