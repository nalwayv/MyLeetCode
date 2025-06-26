class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _get_tree_sum_and_count(self, root: TreeNode|None, total: list[int], count: list[int]) -> None:
        if not root:
            return
        
        total[0] += root.val
        count[0] += 1

        self._get_tree_sum_and_count(root.left, total, count)
        self._get_tree_sum_and_count(root.right, total, count)

    def _get_count_were_subtree_average_equals_root(self, root: TreeNode|None, subtree_count: list[int]) -> None:
        if not root:
            return
        
        total: list[int] = [0]
        count: list[int] = [0]
        self._get_tree_sum_and_count(root, total, count)

        if total[0] // count[0] == root.val:
            subtree_count[0] += 1
        
        self._get_count_were_subtree_average_equals_root(root.left, subtree_count)
        self._get_count_were_subtree_average_equals_root(root.right, subtree_count)

    def averageOfSubtree(self, root: TreeNode) -> int:
        subtree_count: list[int] = [0]
        self._get_count_were_subtree_average_equals_root(root, subtree_count)
        return subtree_count[0]

    
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