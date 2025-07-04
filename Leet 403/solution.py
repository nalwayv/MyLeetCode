class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.prev: Node|None = None
        self.next: Node|None = None
        self.child: Node|None = None


class Solution:
    """
    You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

    Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

    Return the head of the flattened list.
    
    The nodes in the list must have all of their child pointers set to null.
    
    Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
    
    Output: [1,2,3,7,8,11,12,9,10,4,5,6]

    """
    def flatten(self, head: Node|None) -> Node|None:
        """
        flattern using dfs stack
        then rebuild a new Double LInked List
        """
        stk: list[Node|None] = [head]

        h: Node|None = None
        t: Node|None = None

        while stk:
            current: Node|None = stk.pop()

            if current:
                val: int = current.val
                
                if h == None:
                    h = Node(val)
                    t = h
                elif t != None:
                    n = Node(val)
                    t.next = n
                    n.prev = t
                    t = t.next

                stk.append(current.next)

                if current.child:
                    stk.append(current.child)

        return h
    
    def print_list(self, head: Node|None) -> None:
        current: Node|None = head
        while current:
            if current.prev:
                print(f"P: {current.prev.val}")

            print(f"C: {current.val}")
            
            if current.next:
                print(f"N: {current.next.val}")

            current = current.next
            print("---")

def main() -> None:
    solution = Solution()
    
    a: Node|None = Node(1)
    b: Node|None = Node(2)
    c: Node|None = Node(3)
    d: Node|None = Node(4)
    e: Node|None = Node(5)
    f: Node|None = Node(6)

    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    c.next = d
    d.prev = c
    d.next = e
    e.prev = d
    e.next = f
    f.prev = e

    g: Node|None = Node(7)
    h: Node|None = Node(8)
    i: Node|None = Node(9)
    j: Node|None = Node(10)

    g.next = h
    h.prev = g
    h.next = i
    i.prev = h
    i.next = j
    j.prev = i

    k: Node|None = Node(11)
    l: Node|None = Node(12)
    k.next = l
    l.prev = k

    c.child = g
    h.child = k

    a2: Node|None = solution.flatten(a)
    solution.print_list(a2)


if __name__ == "__main__":
    main()