class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    
    def dfs(self, root: TreeNode|None) -> tuple[TreeNode|None, int]:
        if not root:
            return (None, -1)
        
        left, left_depth = self.dfs(root.left)
        right, right_depth = self.dfs(root.right)


        if left_depth == right_depth:
            return (root, left_depth + 1)

        if left_depth > right_depth:
            return (left, left_depth + 1)
        
        return (right, right_depth + 1)


    def lcaDeepestLeaves(self, root: TreeNode|None,) -> TreeNode|None:
        result, _ = self.dfs(root)
        return result
        

def test_case_1(sol: Solution) -> None:
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    result: TreeNode|None = sol.lcaDeepestLeaves(root)
    if result:
        print(f"LCA= {result.val}")
    else:
        print(f"LCA= None")


def test_case_2(sol: Solution) -> None:
    root = TreeNode(1)
    result: TreeNode|None = sol.lcaDeepestLeaves(root)

    if result:
        print(f"LCA= {result.val}")
    else:
        print(f"LCA= None")


def test_case_3(sol: Solution) -> None:
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.right = TreeNode(2)

    result: TreeNode|None = sol.lcaDeepestLeaves(root)
    if result:
        print(f"LCA= {result.val}")
    else:
        print(f"LCA= None")


def main() -> None:
    print("1123. Lowest Common Ancestor of Deepest Leaves")

    sol = Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)


if __name__ == "__main__":
    main()