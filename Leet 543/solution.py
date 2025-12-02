class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def __init__(self) -> None:
        self.result: int = 0

    def diameter(self, root: TreeNode|None) -> int:
        if not root:
            return 0
        
        left: int = self.diameter(root.left)
        right: int = self.diameter(root.right)
        self.result = max(self.result, left + right)

        return 1 + max(left, right)
    

    def diameterOfBinaryTree(self, root: TreeNode|None) -> int:
        if not root:
            return 0
        
        self.result = 0
        self.diameter(root)
        
        return self.result


def main() -> None:
    print('543. Diameter of Binary Tree')

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution() 
    print(solution.diameterOfBinaryTree(root), '== 3')


if __name__ == '__main__':
    main()