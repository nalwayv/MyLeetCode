class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.children: list[Node|None] = []


class Solution:
    def postorder(self, root: Node|None) -> list[int]:
        def get_postorder_values(root: Node|None, result: list[int]) -> None:
            if root == None:
                return

            for child in root.children:
                get_postorder_values(child, result)

            result.append(root.val)


        result: list[int] = []
        get_postorder_values(root, result)

        return result


def print_list(arr: list[int]) -> None:
    n: int = len(arr)
    print("[", end="")
    for idx, val in enumerate(arr):
        if idx + 1 >= n:
            print(f" {val} ", end="")
        else:
            print(f" {val}, ", end="")

    print("]")


def example1(sol: Solution) -> None:
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    a.children = [c,b,d]
    c.children = [e,f]
    
    print_list(sol.postorder(a))

def example2(sol: Solution) -> None:
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)
    i = Node(9)
    j = Node(10)
    k = Node(11)
    l = Node(12)
    m = Node(13)
    n = Node(14)

    a.children = [b,c,d,e]
    c.children = [f,g]
    d.children = [h]
    e.children = [i,j]
    g.children = [k]
    h.children = [l]
    i.children = [m]
    k.children = [n]
    
    print_list(sol.postorder(a))


def main() -> None:
    print("590. N-ary Tree Postorder Traversal")

    sol = Solution()
    
    example1(sol)
    example2(sol)


if __name__ == "__main__":
    main()