class TreeNode:
    def __init__(self, val: int = 0) -> None:
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _build(self, nums: list[int], lo: int, hi: int) -> TreeNode|None:
        if lo > hi:
            return None
        
        mid: int = (lo + hi) // 2
        node: TreeNode|None = TreeNode(nums[mid])
        node.left = self._build(nums, lo, mid - 1)
        node.right = self._build(nums, mid + 1, hi)

        return node

    def _get_values(self, root: TreeNode|None, values: list[int]):
        if not root:
            return
        
        values.append(root.val)
        self._get_values(root.left, values)
        self._get_values(root.right, values)

    def balanceBST(self, root: TreeNode|None) -> TreeNode|None:
        values: list[int] = []
        self._get_values(root, values)
        values.sort()
        return self._build(values, 0, len(values)-1)


def _print_tree(root: TreeNode|None):
    if root == None:
        return
    
    print(f" {root.val} ",end="")
    _print_tree(root.left)
    _print_tree(root.right)


def print_tree(root: TreeNode|None):
    print("[",end="")
    _print_tree(root)
    print("]")


def main() -> None:
    print("1382. Balance a Binary Search Tree")

    sol = Solution()

    print("Case 1")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    print_tree(sol.balanceBST(root))

    print("Case 2")
    root2 = TreeNode(2)
    root2.right = TreeNode(1)
    root2.left = TreeNode(3)
    print_tree(sol.balanceBST(root2))


if __name__ == "__main__":
    main()