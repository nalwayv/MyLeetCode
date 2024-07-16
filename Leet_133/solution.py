# Definition for a Node.
class Node:
    def __init__(self, value: int):
        self.val: int = value
        self.neighbors: list[Node|None] = []

    def __str__(self) -> str:
        return f"{self.val}"

class Solution:
    """
    Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
    """
    def dfs_search(self, current: Node|None, vis: dict[Node|None, Node|None]) ->Node|None:
        if not current:
            return None

        if current in vis:
            return vis[current]
        
        node: Node|None = Node(current.val)
        vis[current] = node

        for nei in current.neighbors:
            node.neighbors.append(self.dfs_search(nei, vis))

        return node

    def cloneGraph(self, node: Node|None) -> Node|None:
        if not node:
            return None
        vis: dict[Node|None, Node|None] = {}
        return self.dfs_search(node, vis)

    def cloneGraph1(self, node: Node|None) -> Node|None:
        if node == None:
            return None
        
        stk: list[Node|None] = [node]
        vis: dict[Node|None, Node|None] = {}

        vis[node] = Node(node.val)

        while stk:
            curr: Node|None = stk.pop()
            
            if curr == None:
                continue

            for n in curr.neighbors:
                if n == None:
                    continue

                if n not in vis:
                    vis[n] = Node(n.val)
                    stk.append(n)
                
                pt: Node|None = vis[curr]
                if pt != None:
                    pt.neighbors.append(vis[n])

        return vis[node]


def print_graph(graph: Node|None) -> None:
    stk: list[Node|None] = [graph]
    vis: set[Node|None] = set()

    while stk:
        current: Node|None = stk.pop()
        if current == None:
            continue

        if current in vis:
            continue
        
        vis.add(current)

        print(f"NODE: {current.val}", end="[")
        
        for nei in current.neighbors:
            if nei == None:
                continue
            print(f"{nei}", end=" ")
            stk.append(nei)

        print("]")


def test1(s: Solution) -> None:
    # [[2,4],[1,3],[2,4],[1,3]]
    print("Test: 1")
    a: Node|None = Node(1)
    b: Node|None = Node(2)
    c: Node|None = Node(3)
    d: Node|None = Node(4)

    a.neighbors = [b, d]
    b.neighbors = [a, c]
    c.neighbors = [b, d]
    d.neighbors = [a, c]
    print_graph(s.cloneGraph1(a))


def test2(s: Solution) -> None:
    # [[]]
    print("Test: 2")
    a: Node|None = Node(1)
    print_graph(s.cloneGraph1(a))


def main() -> None:
    solution = Solution()

    test1(solution)
    test2(solution)


if __name__ == "__main__":
    main()