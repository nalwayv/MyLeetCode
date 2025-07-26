class TreeNode:
    def __init__(self, val: int = 0) -> None:
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def __init__(self) -> None:
        self._value: int = 0

    def _traverse_tree(self, root: TreeNode|None) -> TreeNode|None:
        if not root:
            return
        
        self._traverse_tree(root.right)

        self._value += root.val
        root.val = self._value

        self._traverse_tree(root.left)

    def bstToGst(self, root: TreeNode|None) -> TreeNode|None:
        """
        Convert tree to a Greater Tree such that every key of the original BST is changed to the original key 
        plus the sum of all keys greater than the original key in BST.
        """
        if not root:
            return
        
        self._value = 0

        # update right
        self._traverse_tree(root.right)

        # update root
        self._value += root.val
        root.val = self._value

        # update left
        self._traverse_tree(root.left)

        return root


def print_tree(root: TreeNode|None) -> None:
    if not root:
        return
    
    print_tree(root.right)
    print(root.val)
    print_tree(root.left)


def main() -> None:
    print("1038. Binary Search Tree to Greater Sum Tree")

    root = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)

    sol = Solution()

    print("case 1")
    
    print("before")
    print_tree(root)
    
    print("after")
    result = sol.bstToGst(root)
    print_tree(result)


if __name__ == "__main__":
    main()