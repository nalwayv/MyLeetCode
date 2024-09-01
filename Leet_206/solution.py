class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


class Solution:
    """
    Reverse a linked list
    """

    #--- recursive
    def reverseList_R(self, head: ListNode|None) -> ListNode|None:
        def reverse(a: ListNode|None, b: ListNode|None) -> ListNode|None:
            if a == None:
                return b

            n: ListNode|None = a.next
            a.next = b
            
            return reverse(n, a)
        
        return reverse(head, None)

    #---
    
    def reverseList(self, head: ListNode|None) -> ListNode|None:
        if not head:
            return head
    
        reversed: ListNode|None = None # reversed
        current: ListNode|None = head

        while current:
            next: ListNode|None = current.next
            current.next = reversed
            reversed = current
            current = next

        return reversed

    def print_list(self, head: ListNode|None) -> None:
        if head == None:
            print("None")
            return
        
        i: int = 1
        current: ListNode|None = head
        while current:
            print(f"Node( {current.val} )")
            current = current.next
            i+=1


def main() -> None:
    a: ListNode|None = ListNode(1)
    b: ListNode|None = ListNode(2)
    c: ListNode|None = ListNode(3)

    a.next = b
    b.next = c

    solution = Solution()

    d = solution.reverseList(a)
    solution.print_list(d)


if __name__ == "__main__":
    main()