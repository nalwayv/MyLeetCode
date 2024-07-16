class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    """
    Leet 112 Path Sum.
    """
    def hasPathSum(self, root: TreeNode|None, targetSum: int) -> bool:
        if root == None:
            return False

        stk: list[tuple[TreeNode|None, int]] = [(root, targetSum - root.val)]

        while stk:
            curr_n, curr_s = stk.pop()

            if curr_n == None:
                continue
            
            if curr_n.left == None and curr_n.right == None:
                if curr_s == 0:
                    return True

            if curr_n.left != None:
                stk.append((curr_n.left, curr_s - curr_n.left.val))
            
            if curr_n.right != None:
                stk.append((curr_n.right, curr_s - curr_n.right.val))
                
        return False