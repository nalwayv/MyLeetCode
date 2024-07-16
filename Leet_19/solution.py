class ListNode:
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.next:ListNode|None = None


class Solution:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Example:

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    """
    def get_length(self, headA: ListNode|None) -> int:
        if headA == None:
            return 0
        
        n: int = 0
        current: ListNode|None = headA
        while current:
            current = current.next
            n += 1

        return n
    
    def remove_at_front(self, head: ListNode|None) -> ListNode|None:
        return head.next if head else head

    def remove_at_nth(self, head: ListNode|None, n: int) -> ListNode|None:
        prev: ListNode|None = None
        current: ListNode|None = head

        while n > 0 and current and current.next:
            n -= 1
            prev = current
            current = current.next

        if prev and current:
            prev.next = current.next

        return head

    def remove_nth_from_end(self, head: ListNode|None, n: int) -> ListNode|None:
        """Todo
        """
        nth: int = 1 if n <= 1 else n
        length: int = self.get_length(head)

        if nth > length:
            return head
        
        at: int = length - nth
        
        if at == 0:
            head = self.remove_at_front(head)

        else:
            head = self.remove_at_nth(head, at)

        return head
    
    def print_list(self, head: ListNode|None) -> None:
        if head == None:
            print("None")

        i: int = 0
        current: ListNode|None = head
        while current:
            print(f"At {i}: {current.val}")
            current = current.next
            i+=1


def case1() -> None:
    a: ListNode|None = ListNode(1)# 5
    b: ListNode|None = ListNode(2)# 4
    c: ListNode|None = ListNode(3)# 3
    d: ListNode|None = ListNode(4)# 2
    e: ListNode|None = ListNode(5)# 1
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    n: int = 2

    # a: ListNode|None = ListNode(1)# 2
    # b: ListNode|None = ListNode(2)# 1
    # a.next = b
    # n: int = 2

    # a: ListNode|None = ListNode(1)# 1
    # n: int = 1

    solution = Solution()
    a = solution.remove_nth_from_end(a, n)
    solution.print_list(a)

def main() -> None:
    case1()


if __name__ == "__main__":
    case1()