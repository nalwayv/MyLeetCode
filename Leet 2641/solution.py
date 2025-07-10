class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def replaceValueInTree(self, root: TreeNode|None) -> TreeNode|None:
        if not root:
            return
        
        que: list[TreeNode|None] = [root]
        level_sum: int = root.val

        while que:

            level: int = 0
            
            for _ in range(len(que)):
                curr = que.pop(0)
                if not curr:
                    continue
                
                curr.val = level_sum - curr.val

                value: int = 0
                if curr.left:
                    value += curr.left.val
                if curr.right:
                    value += curr.right.val

                if curr.left:
                    level += curr.left.val
                    curr.left.val = value
                    que.append(curr.left)

                if curr.right:
                    level += curr.right.val
                    curr.right.val = value
                    que.append(curr.right)

            level_sum = level
        
        return root


def print_tree(root: TreeNode|None) -> None:
    if not root:
        return
    
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


def case_1(sol: Solution) -> None:
    print("case 1")
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(10)
    root.right.right = TreeNode(7)

    print_tree(sol.replaceValueInTree(root))


def case_2(sol: Solution) -> None:
    print("case 2")
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    print_tree(sol.replaceValueInTree(root))


def main() -> None:
    print("2641. Cousins in Binary Tree II")

    sol = Solution()

    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()