class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next:ListNode|None = None

class Solution:
    """
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.

    You must solve the problem in O(1) extra space complexity and O(n) time complexity.
    """
    def odd_even_list(self, head: ListNode|None) -> ListNode|None:
        # Used to build both even and odd lists
        even_start: ListNode|None = None
        even_end: ListNode|None = None
        odd_start: ListNode|None = None
        odd_end: ListNode|None = None
        current: ListNode|None = head

        i: int = 1
        while current:
            # EVEN
            if (i & 1) == 0:
                if not even_start:
                    even_start = ListNode(current.val)
                    even_end = even_start
                elif even_end:
                    even_end.next = ListNode(current.val)
                    even_end = even_end.next
            # ODD
            else:
                if not odd_start:
                    odd_start = ListNode(current.val)
                    odd_end = odd_start
                elif odd_end:
                    odd_end.next = ListNode(current.val)
                    odd_end = odd_end.next

            current = current.next
            i += 1

        # concat 'even' onto the end of 'odd'
        if odd_end:
            odd_end.next = even_start

        return odd_start

    def print_list(self, head: ListNode|None) -> None:
        if head == None:
            print("None")
        else:
            current: ListNode|None = head
            while current:
                print(f": {current.val}")
                current = current.next

def main() -> None:
    a: ListNode|None = ListNode(2)
    b: ListNode|None = ListNode(1)
    c: ListNode|None = ListNode(3)
    d: ListNode|None = ListNode(5)
    e: ListNode|None = ListNode(6)
    f: ListNode|None = ListNode(4)
    g: ListNode|None = ListNode(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    solution = Solution()

    a = solution.odd_even_list(a)
    solution.print_list(a)


if __name__ == "__main__":
    main()