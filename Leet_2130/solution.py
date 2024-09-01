class ListNode:
    """ Definition for singly-linked list.
    """
    def __init__(self, val:int=0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def pairSum(self, head: ListNode|None) -> int:
        # Populate list
        
        def populate_from_linkedlist(head: ListNode|None, nums: list[int]):
            if head == None:
                return
            nums.append(head.val)
            populate_from_linkedlist(head.next, nums)
        nums: list[int] = []
        populate_from_linkedlist(head, nums)

        # Reverse second half

        n: int = len(nums)
        p1: int = (n//2)
        p2: int = n-1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1

        # Get max pair

        max_sum: int = 0
        p1 = 0
        p2 = n//2
        while p2 < n:
            num_p1: int = nums[p1]
            num_p2: int = nums[p2]
            max_sum = max(max_sum, num_p1+num_p2)
            p1 += 1
            p2 += 1

        return max_sum


def create_ll_from_arr(values: list[int]):
    head: ListNode|None = None
    tail: ListNode|None = None

    for val in values:
        if head == None:
            head = ListNode(val)
            tail = head
        elif tail:
            tail.next = ListNode(val)
            tail = tail.next

    return head


def case1(sol: Solution) -> None:
    values: list[int] = [5,4,2,1]
    ll: ListNode|None = create_ll_from_arr(values)
    result: str = "pass" if sol.pairSum(ll) == 6 else "fail"
    print(f"case1 {result}")


def case2(sol: Solution) -> None:
    values: list[int] = [4,2,2,3]
    ll: ListNode|None = create_ll_from_arr(values)
    result: str = "pass" if sol.pairSum(ll) == 7 else "fail"
    print(f"case2 {result}")


def case3(sol: Solution) -> None:
    values: list[int]= [1,100000]
    ll: ListNode|None = create_ll_from_arr(values)
    result: str = "pass" if sol.pairSum(ll) == 100001 else "fail"
    print(f"case3 {result}")


def case4(sol: Solution) -> None:
    values: list[int]= [100000,3,32323,10000,3,12,10,666]
    ll: ListNode|None = create_ll_from_arr(values)
    result: str = "pass" if sol.pairSum(ll) == 100666 else "fail"
    print(f"case3 {result}")


def main() -> None:
    print("2130. Maximum Twin Sum of a Linked List")
    
    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)


if __name__ == "__main__":
    main()