class TreeNode(object):
    def __init__(self, value: int):
        self.val: int = value
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def check(self, a: TreeNode|None, b: TreeNode|None) ->bool:
        if not a and not b:
            return True
        
        if a and b:
            return a.val == b.val and self.check(a.left, b.left) and self.check(a.right, b.right)

        return False

    def isSubtree(self, root: TreeNode|None, subRoot: TreeNode|None) -> bool:

        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.check(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# ** Test Cases **


def test_case_1(sol: Solution) -> None:
    print("Case 1 sub should be a subtree of root")
    
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    sub = TreeNode(4)
    sub.left = TreeNode(1)
    sub.right = TreeNode(2)

    result: str = "pass" if sol.isSubtree(root, sub) else "fail"
    print(f"Result: {result}")


def test_case_2(sol: Solution) -> None:
    print("Case 2 sub should not be a subtree of root")
    
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)

    sub = TreeNode(4)
    sub.left = TreeNode(1)
    sub.right = TreeNode(2)

    result: str = "pass" if sol.isSubtree(root, sub) == False else "fail"
    print(f"Result: {result}")


def test_case_3(sol: Solution) -> None:
    print("Case 3 sub should not be a subtree of root")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sub = TreeNode(1)
    sub.left = TreeNode(2)

    result: str = "pass" if sol.isSubtree(root, sub) == False else "fail"
    print(f"Result: {result}")


# ** Main **


def main() -> None:
    print("572. Subtree of Another Tree")
    sol = Solution()

    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)


if __name__ == "__main__":
    main()