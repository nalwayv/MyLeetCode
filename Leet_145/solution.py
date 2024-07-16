class TreeNode:
    def __init__(self, val:int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None

class Solution:
    """
    Leet 145 Binary Tree Postorder Traversal.

    Given the root of a binary tree, return the postorder traversal of its nodes' values.
    """
    def postorderTraversal(self, root: TreeNode|None) -> list[int]:
        def update_results(root: TreeNode|None, result: list[int]) -> None:
            if root == None:
                return

            update_results(root.left, result)
            update_results(root.right, result)
            result.append(root.val)

        result: list[int] = []
        update_results(root, result)
        return result