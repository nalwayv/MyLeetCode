class ListNode:
    def __init__(self, val:int=0):
        self.val: int = val
        self.next: ListNode|None = None


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode|None) -> ListNode|None:
        def remove_nodes(head: ListNode|None, lookup: set[int]) -> ListNode|None:
            """remove any node that have a values that is contained within the lookup
            """
            if not head:
                return None
            
            if head.val in lookup:
                link: ListNode|None = head.next
                return (remove_nodes(link, lookup))

            head.next = remove_nodes(head.next, lookup)
            return head
        
        lookup: set[int] = set()
        for num in nums:
            lookup.add(num)

        head = remove_nodes(head, lookup)
        return head


def print_listnode(head: ListNode|None) -> None:
    if head == None:
        return
    
    current: ListNode|None = head
    while current:
        print(f"{current.val}",end="")
        if current.next != None:
            print("-> ",end="")
        current = current.next
    print("")


def create_listnode(nums: list[int]) -> ListNode|None:
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
    nums: list[int] = [1,2,3]
    values: list[int] = [1,2,3,4,5]
    head: ListNode|None = create_listnode(values)

    print("case 1")
    print_listnode(head)
    head = sol.modifiedList(nums, head)
    print_listnode(head)


def case2(sol: Solution) -> None:
    nums: list[int] = [1]
    values: list[int] = [1,2,1,2,1,2]
    head: ListNode|None = create_listnode(values)
   
    print("case 2")
    print_listnode(head)
    head = sol.modifiedList(nums, head)
    print_listnode(head)


def case3(sol: Solution) -> None:
    nums: list[int] = [5]
    values: list[int] = [1,2,3,4]
    head: ListNode|None = create_listnode(values)

    print("case 3")
    print_listnode(head)
    head = sol.modifiedList(nums, head)
    print_listnode(head)


def main() -> None:
    print("3217. Delete Nodes From Linked List Present in Array")
    
    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()