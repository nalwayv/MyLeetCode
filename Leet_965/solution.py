class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _gather_values_from_tree(self, root: TreeNode|None, values: list[int]) -> None:
        """Populate values list with with those gathered from the tree
        """
        if not root:
            return
        
        values.append(root.val)
        
        self._gather_values_from_tree(root.left, values)
        self._gather_values_from_tree(root.right, values)

    def isUnivalTree(self, root: TreeNode|None) -> bool:
        """A tree is univalued if all values are the same
        """
        if not root:
            return False

        values: list[int] = []
        self._gather_values_from_tree(root, values)

        for i in range(1, len(values)):
            if values[0] != values[i]:
                return False
        
        return True


def main() -> None:
    print("965. Univalued Binary Tree")

    a: TreeNode = TreeNode(1)
    b: TreeNode = TreeNode(1)
    c: TreeNode = TreeNode(1)
    d: TreeNode = TreeNode(1)
    e: TreeNode = TreeNode(1)
    f: TreeNode = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    sol = Solution()
    print(sol.isUnivalTree(a))


if __name__ == "__main__":
    main()