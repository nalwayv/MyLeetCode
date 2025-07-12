class TreeNode:
    def __init__(self, value: int) -> None:
        self.val: int = value
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def insert(self, root: TreeNode|None, value: int) -> TreeNode|None:
        if root == None:
            return TreeNode(value)
        
        if root.val > value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        
        return root
    
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode|None:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.insert(root, preorder[i])
        return root


def print_preorder(root: TreeNode|None) -> None:
    if not root:
        return
    
    print(root.val)

    print_preorder(root.left)
    print_preorder(root.right)


def case1(sol: Solution) -> None:
    print("case 1")

    preorder_nums: list[int] = [8, 5, 10, 1, 7, 12]
    sol = Solution()
    root = sol.bstFromPreorder(preorder_nums)
    print_preorder(root)


def case2(sol: Solution) -> None:
    print("case 2")

    preorder_nums: list[int] = [1, 3]
    sol = Solution()
    root = sol.bstFromPreorder(preorder_nums)
    print_preorder(root)


def main() -> None:
    print("1008. Construct Binary Search Tree from Preorder Traversal")
    
    sol = Solution()

    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()