import math


class ListNode:
    def __init__(self, val:int=0):
        self.val:int = val
        self.next: ListNode|None = None


class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode|None) -> ListNode|None:
        current: ListNode|None = head
        prev: ListNode|None = None

        while current:
            if prev and current:
                gcd: int = math.gcd(prev.val, current.val)
                new_node: ListNode|None = ListNode(gcd)

                new_node.next = current
                prev.next = new_node

            prev = current
            current = current.next

        return head


def create_linked_list(values: list[int]) -> ListNode|None:
    head: ListNode|None = None
    tail: ListNode|None = None
    for value in values:
        if not head:
            head = ListNode(value)
            tail = head
        elif tail:
            tail.next = ListNode(value)
            tail = tail.next
    return head


def print_linked_list(head: ListNode|None) -> None:
    current: ListNode|None = head
    print("[",end="")
    while current:
        print(f" {current.val} ",end="")
        current = current.next
    print("]")


def case_1(sol: Solution) -> None:
    print("case 1")

    values: list[int] = [18, 6, 10, 3]
    head: ListNode|None = create_linked_list(values)
    print_linked_list(head)

    head = sol.insertGreatestCommonDivisors(head)
    print_linked_list(head)
    

def case_2(sol: Solution) -> None:
    print("case 2")

    values: list[int] = [7]
    head: ListNode|None = create_linked_list(values)
    print_linked_list(head)

    head = sol.insertGreatestCommonDivisors(head)
    print_linked_list(head)


def case_3(sol: Solution) -> None:
    print("case 3")

    values: list[int] = [1, 2, 3]
    head: ListNode|None = create_linked_list(values)
    print_linked_list(head)

    head = sol.insertGreatestCommonDivisors(head)
    print_linked_list(head)


def main() -> None:
    print("2807. Insert Greatest Common Divisors in Linked List")
    
    sol = Solution()

    case_1(sol)
    case_2(sol)
    case_3(sol)


if __name__ == "__main__":
    main()
        