class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right : TreeNode|None = None


class Solution:
    def checkTree(self, root: TreeNode|None) -> bool:
        if root == None:
            return False
        
        if root.left == None or root.right == None:
            return False

        parent: int = root.val
        left: int = root.left.val
        right: int = root.right.val

        return (left + right) == parent
    

def case1(sol: Solution) -> None:
    a = TreeNode(10)
    b = TreeNode(4)
    c = TreeNode(6)

    a.left = b
    a.right = c
    
    case1: bool = sol.checkTree(a) == True
    print(f"Case1: {case1}")


def case2(sol: Solution) -> None:
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(1)

    a.left = b
    a.right = c
    
    case1: bool = sol.checkTree(a) == False
    print(f"Case2: {case1}")


def main() -> None:
    solution = Solution()
    case1(solution)
    case2(solution)


if __name__ == "__main__":
    main()