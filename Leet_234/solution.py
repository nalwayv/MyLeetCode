class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next:ListNode|None = None


class Solution:
    """
    """

    def get_n(self, head: ListNode|None, n: int) -> ListNode|None:
        current: ListNode | None = head
        while n > 0 and current:
            current=current.next
            n-=1

        return current
    
    def get_len(self, head: ListNode|None) -> int:
        current: ListNode | None = head
        i = 0
        while current:
            i+=1
            current = current.next
        return i

    def is_pal(self, head: ListNode|None, n: int) -> bool:
        """Using recursion"""
        # get len of list from current head point
        ln: int = self.get_len(head)

        # check if passed the half way pt without any false
        if n > ln // 2:
            return True
        
        # get lo and hi
        lo:ListNode|None = self.get_n(head, n)
        hi:ListNode|None = self.get_n(head, ln - n - 1)
        if lo and hi:
            return lo.val == hi.val and self.is_pal(head, n+1)
        return False
    
    def is_pal_2(self, head:ListNode|None) -> bool:
        """using a stack"""
        lst: list[ListNode] = []
        current: ListNode|None = head
        while current:
            lst.append(current)
            current = current.next

        n: int = len(lst)
        lo: int = 0
        hi: int = n - 1
        while lo < hi:
            if lst[lo].val != lst[hi].val:
                return False
            lo += 1
            hi -= 1
    
        return True
    
    def is_palendrome(self, head: ListNode|None) -> bool:
        use_stk: bool = True

        result: bool = False
        if use_stk:
            print("STACK")
            result = self.is_pal_2(head)
        else:
            # SLOW
            print("RECURSION")
            result = self.is_pal(head, 0)
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
    b: ListNode|None = ListNode(2)
    # c: ListNode|None = ListNode(3)
    # d: ListNode|None = ListNode(4)
    # e: ListNode|None = ListNode(3)
    # f: ListNode|None = ListNode(2)
    # g: ListNode|None = ListNode(1)

    a.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    # e.next = f
    # f.next = g

    solution = Solution()
    print(f"Is palendrome {solution.is_palendrome(a)}")


if __name__ == "__main__":
    main()