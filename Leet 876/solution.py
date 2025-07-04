# 876. Middle of the Linked List
# 
# Given the head of a singly linked list, 
# return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
#

from typing import Optional


class ListNode:
    def __init__(self, val:int =0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: ListNode | None = next


def add(head: Optional[ListNode], node: Optional[ListNode]):
    if not head:
        return
    
    if not head.next:
        head.next = node
    else:
        end: Optional[ListNode] = head
        while True:
            if end.next:
                end = end.next
            else:
                break

        end.next = node


def print_list(head: Optional[ListNode]) -> None:
    current: Optional[ListNode] = head
    while current:
        print(current.val)
        current = current.next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    data: list[ListNode] = []

    current: Optional[ListNode] = head
    while current:
        data.append(current)
        current = current.next

    middle: int = len(data) // 2

    return data[middle]
        

def middleNodeB(head: Optional[ListNode]) -> Optional[ListNode]:
    """ leet using pointers
    """
    if head == None:
        return None
    
    middle: Optional[ListNode] = head
    end: Optional[ListNode] = head

    while end and end.next:
        if middle.next:
            middle = middle.next
        end = end.next.next

    return middle

def main() -> None:
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    e = ListNode(6)

    add(head, a)
    add(head, b)
    add(head, c)
    add(head, d)
    add(head, e)

    result = middleNode(head)
    print_list(result)


if __name__ == "__main__":
    main()