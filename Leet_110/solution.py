class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _get_balance(self, root: TreeNode|None) -> int:
        if not root:
            return 0
        
        left: int = self._get_balance(root.left)
        right: int = self._get_balance(root.right)

        print(left, right)

        if left == -1 or right == -1: 
            return -1
        
        if abs(right - left) > 1:
            return -1
        
        return max(left, right) + 1
    
    def isBalanced(self, root: TreeNode|None) -> bool:
        return self._get_balance(root) != -1


def case1(sol: Solution):
    print("Case 1: ")

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(sol.isBalanced(root))
    print("")


def case2(sol: Solution):
    print("Case 2: ")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    
    print(sol.isBalanced(root))
    print("")


def main() -> None:
    print("110. Balanced Binary Tree")
    
    sol = Solution()
    
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()