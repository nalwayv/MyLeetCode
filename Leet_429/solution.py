from collections import deque


class Node:
    def __init__(self, val:int) -> None:
        self.val = val
        self.children: list[Node|None] = []


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:
        result: list[list[int]] = []        

        que: deque[Node|None] = deque()
        que.append(root)
        
        while que:
            n: int = len(que)
            values: list[int] = []
            for _ in range(n):
                current = que.popleft()
                
                if not current:
                    continue

                values.append(current.val)
                for child in current.children:
                    que.append(child)

            if values:
                result.append(values)

        return result


def case1(sol: Solution) -> None:
    root = Node(1)
    a = Node(3)
    b = Node(2)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    root.children = [a,b,c]
    a.children = [d,e]

    results: list[list[int]] = sol.levelOrder(root)
    print("Case1: [ ", end="")
    for result in results:
        print("[",end="")
        for num in result:
            print(f" {num} ", end="")
        print("] ",end="")
    print("]")


def main() -> None:
    print("429. N-ary Tree Level Order Traversal")
    
    sol = Solution()
    case1(sol)


if __name__ == "__main__":
    main()