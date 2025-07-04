class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _get_leafs(self, root: TreeNode|None, result: list[int]):
        if not root:
            return

        # is leaf
        if not root.left and not root.right:
            result.append(root.val)
        
        self._get_leafs(root.left, result)
        self._get_leafs(root.right, result)
    
    def _get_tree_leafs(self, root: TreeNode|None) -> list[int]:
        result: list[int] = []
        self._get_leafs(root, result)
        return result

    def leafSimilar(self, root1: TreeNode|None, root2: TreeNode|None) -> bool:
        leafs1: list[int] = self._get_tree_leafs(root1)
        leafs2: list[int] = self._get_tree_leafs(root2)

        if len(leafs1) != len(leafs2):
            return False

        for v1,v2 in zip(leafs1, leafs2):
            if v1 != v2:
                return False
        return True


def case1(sol: Solution):
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c

    a1 = TreeNode(1)
    b1 = TreeNode(2)
    c1 = TreeNode(3)
    a1.left = c1
    a1.right = b1

    result: bool = sol.leafSimilar(a, a1)
    print(f"case2 { "pass" if not result else "fail" }")


def main() -> None:
    print("872. Leaf-Similar Trees")

    sol = Solution()
    case1(sol)


if __name__ == "__main__":
    main()