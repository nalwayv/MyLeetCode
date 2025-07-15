class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _populate_values(self, root: TreeNode|None, values: list[int]):
        if not root:
            return
        values.append(root.val)
        self._populate_values(root.left, values)
        self._populate_values(root.right, values)

    def getAllElements(self, root1: TreeNode|None, root2: TreeNode|None) -> list[int]:
        values: list[int] = []
        self._populate_values(root1, values)
        self._populate_values(root2, values)
        values.sort()
        return values


def main() -> None:
    print("1305. All Elements in Two Binary Search Trees")

    root_1 = TreeNode(2)
    root_1.left = TreeNode(1)
    root_1.right = TreeNode(4)

    root_2 = TreeNode(1)
    root_2.left = TreeNode(0)
    root_2.right = TreeNode(3)

    sol = Solution()
    print(sol.getAllElements(root_1, root_2))
     

if __name__ == "__main__":
    main()