class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next:ListNode|None = None


class Solution:
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example:
    
    Input: list1 = [1,2,4], list2 = [1,3,4]
    
    Output: [1,1,2,3,4,4]
    """
    def mergeTwoLists(self, list1: ListNode|None, list2: ListNode|None) -> ListNode|None:
        # STORE DATA INTO LIST FOR QUICK ACCESS
        data: list[int] = []

        # COPY DATA INTO LIST
        m: int = 0
        current: ListNode|None = list1
        while current:
            data.append(current.val)
            current = current.next
            m += 1

        n: int = 0
        current = list2
        while current:
            data.append(current.val)
            current = current.next
            n += 1

        # BUILD NEW LIST USING MERGE

        lo: int = 0
        hi: int = m + n
        mid: int = m

        p1: int = 0
        p2: int = mid

        head: ListNode|None = None
        end: ListNode|None = None

        for _ in range(lo, hi):
            if p1 < mid and (p2 >= hi or data[p1] <= data[p2]):
                if not head:
                    head = ListNode(data[p1])
                    end = head
                elif end:
                    end.next = ListNode(data[p1])
                    end = end.next
                p1 += 1

            else:
                if not head:
                    head = ListNode(data[p2])
                    end = head
                elif end:
                    end.next = ListNode(data[p2])
                    end = end.next
                p2 += 1

        return head

    def mergeTwoLists2(self, list1: ListNode|None, list2: ListNode|None) -> ListNode|None:
        """
        using recursion
        """
        if not list1:
            # print("B\n")
            return list2

        if not list2:
            # print("A\n")
            return list1

        if list1.val < list2.val:
            # print("A, A-> = (A->, B)")
            list1.next = self.mergeTwoLists2(list1.next, list2)
            # self.print_list(list1)
            return list1

        else:
            # print("B, B-> = (A, B->)")
            list2.next = self.mergeTwoLists2(list1, list2.next)
            # self.print_list(list2)
            return list2
        

    def mergeTwoLists3(self, list1: ListNode|None, list2: ListNode|None):
        current: ListNode|None = ListNode(0)
        prev: ListNode|None = current

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2

        if list1 != None or list2 != None:
            current.next = list1 if list1 != None else list2

        return prev.next

    def print_list(self, ls: ListNode|None) -> None:
        current: ListNode | None = ls
        # str_num:list[str] = []
        print("", end="")
        while current:
            print(f"{current.val} -> ", end="")
            # str_num.append(str(current.val))
            current = current.next
        print("X")
        # print(" -> ".join(str_num))


def main() -> None:
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    a.next = b
    b.next = c

    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)
    d.next = e
    e.next = f

    solution = Solution()
    h: ListNode | None = solution.mergeTwoLists3(a, d)
    solution.print_list(h)

if __name__ == "__main__":
    main()