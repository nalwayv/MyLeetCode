class TreeNode(object):
    def __init__(self, value: int):
        self.val: int = value
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def calculate(self, root: TreeNode|None, ref: list[int]) -> int:
        if not root:
            return 0

        left: int = self.calculate(root.left, ref)
        right: int = self.calculate(root.right, ref)
        
        ref[0] += abs(left - right)

        return root.val + left + right

    def findTilt(self, root: TreeNode|None) -> int:
        result: list[int] = [0]
        self.calculate(root, result)
        return result[0]


def case_1(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    result: int = sol.findTilt(root)
    test: str = "pass" if result == 1 else "fail"
    print(f"Case 1: {test}")


def case_2(sol: Solution) -> None:
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right = TreeNode(9)
    root.right.right = TreeNode(7)

    result: int = sol.findTilt(root)
    test: str = "pass" if result == 15 else "fail"
    print(f"Case 2: {test}")


def case_3(sol: Solution) -> None:
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(3)

    root.right = TreeNode(14)
    root.right.right = TreeNode(2)
    root.right.left = TreeNode(2)

    result: int = sol.findTilt(root)
    test: str = "pass" if result == 9 else "fail"
    print(f"Case 3: {test}")


def main() -> None:
    print("563. Binary Tree Tilt")

    sol = Solution()
    
    case_1(sol)
    case_2(sol)
    case_3(sol)


if __name__ == "__main__":
    main()