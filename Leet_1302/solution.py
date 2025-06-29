class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def get_max_sum(self, depth: int, root: TreeNode|None, max_sum: list[int],  max_depth: list[int]):
        if not root:
            return

        # reset max sum
        if depth > max_depth[0]:
            max_depth[0] = depth
            max_sum[0] = 0
        
        if depth == max_depth[0]:
            max_sum[0] += root.val

        self.get_max_sum(depth + 1, root.left, max_sum, max_depth)
        self.get_max_sum(depth + 1, root.right, max_sum, max_depth)

    def deepestLeavesSum(self, root: TreeNode|None) -> int:
        # ref 
        max_sum: list[int] = [0]
        max_depth: list[int] = [-1]

        self.get_max_sum(0, root, max_sum, max_depth)

        return max_sum[0]


def main() -> None:
    print("1302. Deepest Leaves Sum")

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)

    sol = Solution()
    print(f"Max Depth Sum {sol.deepestLeavesSum(root)}")


if __name__ == "__main__":
    main()