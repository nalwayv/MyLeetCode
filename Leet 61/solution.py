# Definition for singly-linked list.

class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode|None = None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.val})"


class Solution:
    """
    Given the head of a linked list, rotate the list to the right by k places.
    
    Example:

    Input: head = [1,2,3,4,5], k = 2
    
    Output: [4,5,1,2,3]
    """
    def print_list(self, head: ListNode|None) -> None:
        current: ListNode|None = head
        while current:
            print(f"{current.val}")
            current = current.next

    def from_list(self, nums: list[int]) -> ListNode|None:
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

    def get_length(self, head: ListNode|None) -> int:
        count: int = 0
        current: ListNode|None = head
        while current:
            count += 1
            current = current.next
        return count

    def rotateRight(self, head: ListNode|None, k: int) -> ListNode|None:
        # k = 2
        #       5 4 3 2 1
        # in:  [1,2,3,4,5]
        #             |
        # 
        # out: [4,5,1,2,3]
        
        # VERSION 2
        if not head or k == 0:
            return head
        
        n: int = self.get_length(head)
        at: int = (n - k) % n

        # k matches n
        # so just return head
        if at == 0:
            return head

        prev: ListNode|None = None

        # find break point and dissconnect
        # creating new end point
        # start carries on from break point
        start: ListNode|None = head
        while at != 0 and start:
            prev = start
            start = start.next
            at -= 1
        if prev:
            prev.next = None

        # from new start find end
        # and connect back to head
        end: ListNode|None = start
        while end:
            prev = end
            end = end.next
        if prev:
            prev.next = head
            head = start

        return head
    
    # def rotateRight(self, head: ListNode|None, k: int) -> ListNode|None:
        # VERSION 2

        # n: int = self.get_length(head)
        # start_at: int = (n - k) % n # % loop back
        
        # # build new list
        # start: ListNode|None = None
        # end: ListNode|None = None
        # current: ListNode | None = self.get_at(head, start_at)

        # # count: int = n
        # while k != 0:
        #     if current:
        #         if start == None:
        #             start = ListNode(current.val)
        #             end = start
        #         elif end != None:
        #             end.next = ListNode(current.val)
        #             end = end.next

        #         # loop back to head
        #         if current.next == None:
        #             current = head
        #         else:
        #             current = current.next

        #     k -= 1

        # return start

def main() -> None:
    solution = Solution()

    k: int = 2
    head: ListNode | None = solution.from_list([1,2]);
    result: ListNode | None = solution.rotateRight(head, k)
    solution.print_list(result)

if __name__ == "__main__":
    main()