class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def get_count(self, root: TreeNode|None, ref_count: list[int]) -> tuple[int, int]:
        if not root:
            return (0, 0)
        
        left_sum, left_count = self.get_count(root.left, ref_count)
        right_sum, right_count = self.get_count(root.right, ref_count)

        subtree_sum: int = left_sum + right_sum + root.val
        subtree_count: int  = left_count + right_count + 1
        
        if root.val == (subtree_sum // subtree_count):
            ref_count[0] += 1

        return (subtree_sum, subtree_count)

    def averageOfSubtree(self, root: TreeNode) -> int:
        ref_count:list[int] = [0]
        _,_ = self.get_count(root, ref_count)
        return ref_count[0]


# -- TestCases


def case_1(sol: Solution) -> None:
    print("-- Case 1")
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(6)

    sol = Solution()
    count: int = sol.averageOfSubtree(root)
    print(f"Count: {count}")


def case_2(sol: Solution) -> None:
    print("-- Case 2")
    root = TreeNode(1)
    sol = Solution()
    count: int = sol.averageOfSubtree(root)
    print(f"Count: {count}")


# -- Main


def main() -> None:
    print("2265. Count Nodes Equal to Average of Subtree")

    sol = Solution()

    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()
