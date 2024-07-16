from collections import deque
from sys import maxsize


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    """
    Leet 101 Symmetric Tree.

    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    """
    def isSymmetric(self, root: TreeNode|None) -> bool:
        if root == None:
            return False
        
        que: deque[TreeNode|None] = deque()
        que.append(root)
        
        while que:
            ln: int = len(que)
            vals: list[int] = []
            
            for _ in range(ln):
                current: TreeNode|None = que.popleft()
                if current == None:
                    continue
                
                if current.left != None:
                    que.append(current.left)
                    vals.append(current.left.val)
                else:
                    vals.append(maxsize)
                
                if current.right != None:
                    que.append(current.right)
                    vals.append(current.right.val)
                else:
                    vals.append(maxsize)
                    
            if vals:
                p1: int = 0
                p2: int = len(vals) - 1
                
                while p1 < p2:
                    if vals[p1] != vals[p2]:
                        return False
                    p1 += 1
                    p2 -= 1
        
        return True