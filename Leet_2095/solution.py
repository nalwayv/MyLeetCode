class ListNode:
    def __init__(self, val: int=0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def get_length(self, head: ListNode|None) -> int:
        if head == None:
            return 0
        
        n: int = 0
        current: ListNode|None = head
        while current:
            current = current.next
            n += 1

        return n

    def deleteMiddle(self, head: ListNode|None) -> ListNode|None:
        if head == None:
            return head
        
        n: int = self.get_length(head)
        if n == 1:
            head = head.next
        else:

            mid: int = n//2 if (n % 2 == 0) else (n+1)//2
            at: int = n - mid

            prev: ListNode|None = None
            curr: ListNode|None = head
            
            while at > 0 and curr and curr.next:
                at -= 1
                prev = curr
                curr = curr.next

            if prev and curr:
                prev.next = curr.next

        return head
    

def print_list(head: ListNode|None) -> None:
    if head == None:
        print("None")

    current: ListNode|None = head
    while current:
        print(f"{current.val}",end="")
        if current.next != None:
            print("->",end="")
        current = current.next
    print("")


def create_list(nums: list[int]) -> ListNode|None:
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


def case1(sol: Solution) -> None:
    print("CASE 1")
    head = create_list([1,3,4,7,1,2,6])
    print_list(head)
    head = sol.deleteMiddle(head)
    print_list(head)
    print("")


def case2(sol: Solution) -> None:
    print("CASE 2")
    head = create_list([1,2,3,4])
    print_list(head)
    head = sol.deleteMiddle(head)
    print_list(head)
    print("")


def case3(sol: Solution) -> None:
    print("CASE 3")
    head = create_list([2,1])
    print_list(head)
    head = sol.deleteMiddle(head)
    print_list(head)
    print("")


def case4(sol: Solution) -> None:
    print("CASE 4")
    head = create_list([1])
    print_list(head)
    head = sol.deleteMiddle(head)
    print_list(head)
    print("")


def main() -> None:
    print("2095. Delete the Middle Node of a Linked List")
    
    sol = Solution()
   
    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)


if __name__ == "__main__":
    main()