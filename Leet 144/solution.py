class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    """
    Binary Tree Preorder Traversal.

    Given the root of a binary tree, return the preorder traversal of its nodes' values.
    """
    def preorderTraversal(self, root: TreeNode|None) -> list[int]:
        def get_values(root: TreeNode|None, result: list[int]) -> None:
            if root == None:
                return
            
            result.append(root.val)
            
            get_values(root.left, result)
            get_values(root.right, result)

        result: list[int] = []
        get_values(root, result)
        return result
        