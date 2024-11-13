class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: ListNode|None = None


class Solution:
    def hasCycle(self, head: ListNode|None) -> bool:
        if head == None or head.next == None:
            return False
        
        
        slow: ListNode|None = head
        fast: ListNode|None = head
            
        while fast != None and fast.next != None:
            fast = fast.next.next
            if slow:
                slow = slow.next
            
            if fast == slow:
                return True
                
        return False


def build_linked_list(nums: list[int]) -> ListNode:
    n: int = len(nums)
    head = ListNode(nums[0])
    tail = head
    for i in range(1, n):
        #set tail
        tail.next = ListNode(nums[i])
        #move to new endpoint
        tail = tail.next
    return head


def main() -> None:
    head: ListNode = build_linked_list([3, 2, 0, -4])

    # create cycle between 2 and -4
    a: ListNode|None = head.next
    b: ListNode|None = head
    while b and b.next:
        b = b.next  
    b.next = a

    sol = Solution()
    print(sol.hasCycle(head))


if __name__ == "__main__":
    main()