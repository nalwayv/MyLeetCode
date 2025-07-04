class Node:
    def __init__(self, val:int) -> None:
        self.val = val
        self.children: list[Node|None] = []


class Solution:
    @staticmethod
    def _dfs_pre_order(root: Node|None, result: list[int]) -> None:
        """Helper method that populates result list with n_tree values
        """
        if not root:
            return
        
        result.append(root.val)

        for child in root.children:
            Solution._dfs_pre_order(child, result)

    def preorder(self, root: Node) -> list[int]:
        result: list[int] = []
        Solution._dfs_pre_order(root, result)
        return result
    

def main() -> None:
    print("589. N-ary Tree Preorder Traversal")

    root = Node(1)
    a = Node(3)
    b = Node(2)
    c = Node(4)
    d = Node(5)
    e = Node(6)
    root.children = [a,b,c]
    a.children = [d,e]

    sol = Solution()
    result = sol.preorder(root)
    print(f"Case 1: {result}")


if __name__ == "__main__":
    main()