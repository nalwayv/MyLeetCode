class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


class Solution:
    """
    Given the head of a linked list and an integer val, 
    remove all the nodes of the linked list that has Node.val == val, 
    and return the new head.

    Example:

        Input: head = [1,2,6,3,4,5,6], val = 6
    
        Output: [1,2,3,4,5]
    """
    def removeElements(self, head: ListNode|None, val: int) -> ListNode|None:
        if head == None:
            return

        result: ListNode|None = None
        result_at: ListNode|None = None
        current: ListNode|None = head
        while current:
            if current.val != val:
                new_node = ListNode(current.val)
                if not result:
                    result = new_node
                    result_at = result
                elif result_at:
                    result_at.next = new_node
                    result_at = result_at.next

            current = current.next

        return result
    

    def print_list(self, head: ListNode|None) -> None:
        if head == None:
            print("None")
        else:
            current: ListNode|None = head
            while current:
                print(f": {current.val}")
                current = current.next


def main() -> None:
    a: ListNode|None = ListNode(1)
    b: ListNode|None = ListNode(1)
    c: ListNode|None = ListNode(1)
    d: ListNode|None = ListNode(1)
    e: ListNode|None = ListNode(1)
    f: ListNode|None = ListNode(4)
    g: ListNode|None = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f 
    f.next = g

    val: int = 1

    solution = Solution()
    a = solution.removeElements(a, val)
    solution.print_list(a)

if __name__ == "__main__":
    main()