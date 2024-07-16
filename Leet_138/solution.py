"""
138. Copy List with Random Pointer

Make a deep copy of list and preserve its random connections
"""
class Node:
    def __init__(self, x: int):
        self.val:int = x
        self.next:Node|None = None
        self.random:Node|None = None


class Solution:

    def get_length(self, head:Node|None) -> int:
        count: int = 0
        current: Node|None = head
        while current:
            count += 1
            current = current.next
        return count
    
    def find_node(self, node: Node|None, target: Node|None) -> int:
        at: int = 0
        current: Node | None = node
        while current:
            if current == target:
                return at
            at += 1
            current = current.next
        return -1

    def copyRandomList(self, head: Node|None) -> Node|None:
        if not head:
            return None

        n: int = self.get_length(head)
        nodes: list[Node|None] = [None] * n
        start: Node|None = None
        end: Node|None = None

        i: int = 0
        current: Node|None = head
        while current:
            # NEW NODE
            if nodes[i] == None:
                nodes[i] = Node(current.val)

            # CONNECT NEXT
            if nodes[i] and start == None:
                start = nodes[i]
                end = start
            elif nodes[i] and end != None:
                end.next = nodes[i]
                end = end.next

            # CONNECT RNG
            if current.random:
                j: int = self.find_node(head, current.random)
                if j != -1:
                    if nodes[j] == None:
                        nodes[j] = Node(current.random.val)
                        nodes[i].random = nodes[j]
                    else:
                        nodes[i].random = nodes[j]

            i += 1
            current = current.next

        return start

    def print(self, head: Node|None) -> None:
        current: Node | None = head
        while current:
            if current.random:
                print(f"{current.val} -> {current.random.val}")
            else:
                print(current.val)
            
            current = current.next


def main() -> None:
    solution = Solution()

    # CASE 1
    # a = Node(7)
    # b = Node(13)
    # a.next = b
    # b.random = b

    # CASE 2
    a = Node(7)
    b = Node(13)
    c = Node(11)
    d = Node(10)
    e = Node(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    b.random = a
    c.random = e
    d.random = c
    e.random = a

    new_a: Node | None = solution.copyRandomList(a)
    solution.print(new_a)

if __name__ == "__main__":
    main()