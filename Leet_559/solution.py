class Node:
    def __init__(self, val:int) -> None:
        self.val = val
        self.children: list[Node|None] = []


class Solution:
    def maxDepth(self, root: Node|None) -> int:
        """Bottom Up get max depth
        """
        if not root:
            return 0
        
        answer: int = 0
        for child in root.children:
            answer = max(self.maxDepth(child), answer)
        
        return answer + 1


def case1(sol: Solution) -> None:
    root = Node(1)
    a = Node(3)
    b = Node(2)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    root.children = [a,b,c]
    a.children = [d,e]

    result: int = sol.maxDepth(root)
    print(f"Case 1: {result} == 3")


def case2(sol: Solution) -> None:
    root = Node(1)
    a = Node(2)
    b = Node(3)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    f = Node(7)
    g = Node(8)
    h = Node(9)
    i = Node(10)
    j = Node(11)
    k = Node(12)
    l = Node(13)
    m = Node(14)

    root.children = [a,b,c,d]
    b.children = [e,f]
    c.children = [g]
    d.children = [h,i]
    f.children = [j]
    g.children = [k]
    h.children = [l]
    j.children = [m]

    result: int = sol.maxDepth(root)
    print(f"Case 2: {result} == 5")


def main() -> None:
    print("559. Maximum Depth of N-ary Tree")

    sol = Solution()
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()