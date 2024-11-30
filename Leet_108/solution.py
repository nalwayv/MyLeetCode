class TreeNode:
    def __init__(self, val: int = 0) -> None:
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    @staticmethod
    def _build_bst(nums: list[int], lo: int, hi: int) -> TreeNode|None:
        """Helper function to build bst from sorted list
        """
        if lo > hi:
            return None
        
        mid: int = (lo + hi) // 2
        node: TreeNode|None = TreeNode(nums[mid])
        node.left = Solution._build_bst(nums, lo, mid - 1)
        node.right = Solution._build_bst(nums, mid + 1, hi)
        return node

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode|None:
        """Given an integer array nums where the elements are sorted in ascending order, convert it to a
        height-balanced binary search tree.
        """
        return Solution._build_bst(nums, 0, len(nums) - 1)


def _helper_print_inorder(r: TreeNode|None):
    if r == None:
        return
    
    _helper_print_inorder(r.left)
    print(f" {r.val} ",end="")
    _helper_print_inorder(r.right)


def print_inorder(root: TreeNode|None) -> None:
    print("[",end="")
    _helper_print_inorder(root)
    print("]")


def main() -> None:
    print("108. Convert Sorted Array to Binary Search Tree")

    sol = Solution()
    nums: list[int] = [-10,-3,0,5,9]
    result: TreeNode|None = sol.sortedArrayToBST(nums)
    
    print_inorder(result)


if __name__ == "__main__":
    main()