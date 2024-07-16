
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.next: ListNode|None = None

    def __str__(self) -> str:
        return f"Node({self.val})"


def has_cycle(head: ListNode|None) -> bool:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    a -> b -> c -> b
    """
    if head == None or head.next == None:
        return False

    # USING FAST AND SLOW POINTER
    fast: ListNode|None = head
    slow: ListNode|None = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False


def detect_cycle(head: ListNode|None) -> ListNode|None:
    #  USING STACK
    vis: list[ListNode] = []
    current: ListNode|None = head
    while current:
        if current in vis:
            return current
        
        vis.append(current)
        current = current.next
    return None


def detect_cycle3(head: ListNode|None) -> ListNode|None:
    # USING TWO POINTERS
    if head == None or head.next == None:
        return None

    fast: ListNode|None = head
    slow: ListNode|None = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            # from start move p1 until it collides with p2
            p1: ListNode|None = head
            p2: ListNode|None = slow
            while p1 and p2 and p1 != p2:
                p1 = p1.next
                p2 = p2.next

            return p1
        
    return None


def reverse(head: ListNode|None) -> ListNode|None:
    if not head:
        return
    
    reverse: ListNode|None = None # reversed
    current: ListNode|None = head
    while current:
        next: ListNode | None = current.next
        current.next = reverse
        reverse = current
        current = next

    head = reverse


def list_move_to(headA:ListNode|None, n: int) -> ListNode|None:
    current: ListNode|None = headA
    while n != 0 and current:
        n -= 1
        current = current.next

    return current

def list_len(headA:ListNode|None) -> int:
    if headA == None:
        return 0
    
    n: int = 0
    current: ListNode|None = headA
    while current:
        current = current.next
        n += 1

    return n

def list_find_match(headA: ListNode|None, headB: ListNode|None) -> ListNode|None:
    p1: ListNode|None = headA
    p2: ListNode|None = headB
    while p1 and p2 and p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

def intersect(headA: ListNode|None, headB: ListNode|None) -> ListNode|None:
    # USING DICT
    # table: dict[ListNode, bool] = {}
    # current: ListNode|None = headA
    # while current:
    #     table[current] = True
    #     current = current.next
    # current = headB
    # while current:
    #     if current in table:
    #         return current
    #     table[current] = True
    #     current = current.next

    # USING TWO POINTERS
    a: int = list_len(headA)
    b: int = list_len(headB)

    # using diff in length to move a pt to befor checking
    if a == b:
        return list_find_match(headA, headB)
    if a > b:
        return list_find_match(list_move_to(headA, a-b), headB)
    if a < b:
        return list_find_match(headA, list_move_to(headB, b-a))

    return None

def clamp(val:int, lo:int, hi: int) -> int:
    if val <= lo:
        return lo
    if val >= hi:
        return hi
    return val

def nth_end(head: ListNode|None, nth: int) -> ListNode|None:
    p1: ListNode|None = head
    p2: ListNode|None = head

    # pre-move p1 by nth positions
    for _ in range(nth):
        if p1:
            p1 = p1.next
    
    while p1:
        p1 = p1.next
        
        if p2:
            p2 = p2.next

    return p2

def remove_nth_from_end(head: ListNode|None, n: int) -> ListNode|None:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Example:

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    """
    l: int = list_len(head)
    at: int = clamp(l - n, 0, l)
    
    if at == 0:
        if head and head.next:
            head = head.next
            return head
        else:
            return None
        
    prev: ListNode|None = None
    current: ListNode|None = head

    while at != 0 and current and current.next:
        print(f"At: {at}")
        at -= 1
        prev = current
        current = current.next

    if prev and current:
        prev.next = current.next

    return head


def case1() -> None:
    a: ListNode|None = ListNode(5)
    b: ListNode|None = ListNode(6)
    c: ListNode|None = ListNode(1)
    d: ListNode|None = ListNode(8)
    e: ListNode|None = ListNode(4)
    f: ListNode|None = ListNode(5)

    g: ListNode|None = ListNode(4)
    h: ListNode|None = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    g.next = h
    h.next = d

    result: ListNode|None = intersect(a, g)
    print("Should be 8")
    if result:
        print("Result: ", result.val)
    else:
        print("None")


def case3() -> None:
    a: ListNode|None = ListNode(2)
    b: ListNode|None = ListNode(6)
    c: ListNode|None = ListNode(4)

    d: ListNode|None = ListNode(1)
    e: ListNode|None = ListNode(5)

    a.next = b
    b.next = c

    d.next = e


    result: ListNode|None = intersect(a, d)
    print("Should be None")
    if result:
        print("Result: ", result.val)
    else:
        print("None")


def case2() -> None:
    a: ListNode|None = ListNode(1)
    b: ListNode|None = ListNode(9)
    c: ListNode|None = ListNode(1)
    d: ListNode|None = ListNode(2)
    e: ListNode|None = ListNode(4)

    f: ListNode|None = ListNode(3)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    f.next = d

    result: ListNode|None = intersect(a, f)
    print("Should be 2")
    if result:
        print("Result: ", result.val)
    else:
        print("None")


def case4() -> None:
    a: ListNode|None = ListNode(1)
    b: ListNode|None = ListNode(2)
    c: ListNode|None = ListNode(3)
    d: ListNode|None = ListNode(4)
    e: ListNode|None = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    a = remove_nth_from_end(a, 3)
    current: ListNode|None = a
    while current:
        print(current.val)
        current = current.next


def case5() -> None:
    "testing nth"
    a: ListNode|None = ListNode(1)#5
    b: ListNode|None = ListNode(2)#4
    c: ListNode|None = ListNode(3)#3
    d: ListNode|None = ListNode(4)#2
    e: ListNode|None = ListNode(5)#1

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    result: ListNode|None = nth_end(a, 4)
    if result:
        print(f"Nth: {result}")
    else:
        print("error")

def main() -> None:
    # case1()
    # case2()
    # case3()
    # case4()
    case5()

if __name__ == "__main__":
    main()