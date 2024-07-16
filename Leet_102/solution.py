from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    """
    Leet 102 Binary Tree Level Order Traversal.

    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
    
    Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
    """
    def levelOrder(self, root: TreeNode|None) -> list[list[int]]:
        result: list[list[int]] = []
        if root == None:
            return result
        
        top_level: list[int] = [root.val]
        result.append(top_level)

        que: deque[TreeNode|None] = deque()
        que.append(root)
        
        while que:
            
            ln: int = len(que)
            current_level: list[int] = []

            for _ in range(ln):
                current: TreeNode|None = que.popleft()
                if current == None:
                    continue
                
                if current.left != None:
                    que.append(current.left)
                    current_level.append(current.left.val)
                    
                if current.right != None:
                    que.append(current.right)
                    current_level.append(current.right.val)
                    
            if len(current_level) > 0:
                result.append(current_level)
                
        return result