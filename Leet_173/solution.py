class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class BSTIterator:
    def __init__(self, root: TreeNode|None):
        self.at: int = 0
        self.nums: list[int] = []
        self._populate(self.nums, root)

    def _populate(self, nums: list[int], root: TreeNode|None) -> None:
        """Helper to populate self.nums with root's values inorder
        """
        if not root:
            return
        
        self._populate(nums, root.left)
        nums.append(root.val)
        self._populate(nums, root.right)

    def next(self) -> int:
        num: int = self.nums[self.at]
        self.at += 1
        return num

    def hasNext(self) -> bool:
        return self.at < len(self.nums)



# __ HELPERS


def bst_insert(root: TreeNode|None, value: int) -> TreeNode|None:
    if root == None:
        return TreeNode(value)
    
    if root.val > value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    
    return root


def build_tree(nums: list[int]) -> TreeNode|None:
    root: TreeNode|None = None
    
    for num in nums:
        root = bst_insert(root, num)

    return root


def _inorder(root: TreeNode|None):
    if root == None:
        return
    
    _inorder(root.left)
    print(f" {root.val} ", end="")
    _inorder(root.right)


def print_inorder(root: TreeNode|None):
    print("[", end="")
    _inorder(root)
    print("]")


# __ MAIN


def main() -> None:
    print("173. Binary Search Tree Iterator")

    nums: list[int] = [7,3,15,9,20]
    root: TreeNode|None = build_tree(nums)

    bst_itr = BSTIterator(root)

    print(bst_itr.next())    # return 3
    print(bst_itr.next())    # return 7
    print(bst_itr.hasNext()) # return True
    print(bst_itr.next())    # return 9
    print(bst_itr.hasNext()) # return True
    print(bst_itr.next())    # return 15
    print(bst_itr.hasNext()) # return True
    print(bst_itr.next())    # return 20
    print(bst_itr.hasNext()) # return False


if __name__ == "__main__":
    main()