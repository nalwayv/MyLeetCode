class TreeNode(object):
    def __init__(self, value: int) -> None:
        self.val: int = value
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _sum_left(self, root: TreeNode|None, sum_total: list[int]) -> None:
        if not root:
            return
        
        if root.left:
            left: TreeNode = root.left
            if not left.left and not left.right:
                sum_total[0] += left.val

        self._sum_left(root.left, sum_total)
        self._sum_left(root.right, sum_total)

    def sumOfLeftLeaves(self, root: TreeNode|None) -> int:
        sum_total: list[int] = [0]
        self._sum_left(root, sum_total)
        
        return sum_total[0]


def case1(sol: Solution) -> None:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result: int = sol.sumOfLeftLeaves(root)
    print(f"Case 1: {result}")


def case2(sol: Solution) -> None:
    root = TreeNode(0)

    result: int = sol.sumOfLeftLeaves(root)
    print(f"Case 1: {result}")


def main() -> None:
    print("404. Sum of Left Leaves")

    sol = Solution()
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()