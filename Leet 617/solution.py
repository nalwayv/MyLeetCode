class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def mergeTrees(self, root1: TreeNode|None, root2: TreeNode|None) -> TreeNode|None:        
        node: TreeNode|None = None

        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
        elif root1 and not root2:
            node = TreeNode(root1.val)
        elif not root1 and root2:
            node = TreeNode(root2.val)

        if node:
            if root1 and root2:
                node.left = self.mergeTrees(root1.left, root2.left)
                node.right = self.mergeTrees(root1.right, root2.right)
            elif root1 and not root2:
                node.left = self.mergeTrees(root1.left, None)
                node.right = self.mergeTrees(root1.right, None)
            elif not root1 and root2:
                node.left = self.mergeTrees(None, root2.left)
                node.right = self.mergeTrees(None, root2.right)

        return node
    

def _print_tree(root: TreeNode|None) -> None:
    if not root:
        return
    
    print(f" {root.val} ",end="")
    _print_tree(root.left)
    _print_tree(root.right)


def print_tree(root: TreeNode|None) -> None:
    print("[", end="")
    _print_tree(root)
    print("]")


def case_1(sol: Solution) -> None:
    r1 = TreeNode(1)
    r1.left = TreeNode(3)
    r1.right = TreeNode(2)
    r1.left.left = TreeNode(5)

    r2 = TreeNode(2)
    r2.left = TreeNode(1)
    r2.right = TreeNode(3)
    r2.left.right = TreeNode(4)
    r2.right.right = TreeNode(7)

    r3 = sol.mergeTrees(r1, r2)
    print_tree(r3)
        

def main() -> None:
    print("617. Merge Two Binary Trees")

    sol = Solution()
    case_1(sol)


if __name__ == "__main__":
    main()