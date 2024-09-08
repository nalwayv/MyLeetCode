class ListNode:
    def __init__(self, val: int=0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def _get_linked_list_length(self, head: ListNode|None) -> int:
        i: int = 0
        current: ListNode|None = head
        while current:
            i += 1
            current = current.next
        return i

    def splitListToParts(self, head: ListNode|None, k: int) -> list[ListNode|None]:
        n: int = self._get_linked_list_length(head)
        
        result: list[ListNode|None] = []
        
        div,mod = divmod(n, k)

        current: ListNode|None = head
        for i in range(k):        
            chunk: ListNode|None = current

            for _ in range(div + (1 if i < mod else 0) - 1):
                if current:
                    current = current.next

            if current:
                tmp = current.next
                current.next = None
                current = tmp

            result.append(chunk)
        
        return result


def create_linked_list(values: list[int]) -> ListNode|None:
    head: ListNode|None = None
    tail: ListNode|None = None
    for num in values:
        if not head:
            head = ListNode(num)
            tail = head
        elif tail:
            tail.next = ListNode(num)
            tail = tail.next
    return head


def print_linked_list(head: ListNode|None) -> None:
    print("[",end="")
    current: ListNode|None = head
    while current:
        print(f" {current.val} ",end="")
        current = current.next
    print("]")


def case_1(sol: Solution) -> None:
    print("case 1")
    ll: ListNode|None = create_linked_list([1,2,3])
    print_linked_list(ll)
    result: list[ListNode|None] = sol.splitListToParts(ll, 5)
    for res in result:
        print_linked_list(res)


def case_2(sol: Solution) -> None:
    print("case 2")
    ll: ListNode|None = create_linked_list([1,2,3,4,5,6,7,8,9,10])
    result: list[ListNode|None] = sol.splitListToParts(ll, 3)
    for res in result:
        print_linked_list(res)


def main() -> None:
    print("725. Split Linked List in Parts")
    sol = Solution()
    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()