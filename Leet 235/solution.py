from collections import deque


class TreeNode:
    def __init__(self, x: int = 0):
        self.val: int = x
        self.left: TreeNode|None = None
        self.right:TreeNode|None = None


class Solution:
    @staticmethod
    def _dfs(root: TreeNode|None, a: TreeNode, b: TreeNode) -> TreeNode|None:
        """Helper function that does a depth first search and checks if root or its children are 
        a lowest common ancestor node of a and b.
        """
        if not root:
            return None

        if root.val == a.val or root.val == b.val:
            return root

        left = Solution._dfs(root.left, a, b)
        right = Solution._dfs(root.right, a, b)

        if left and right:
            return root
        
        if left:
            return left
        return right
    
    def lowestCommonAncestor(self, root: TreeNode|None, p: TreeNode, q: TreeNode) -> TreeNode|None:
        return self._dfs(root, p, q)


def build_tree(nums: list[int|None]) -> TreeNode|None:
    """build an in-order tree from nums
    """
    if not nums:
        return None
    
    if nums[0] == None:
        return None
    
    root = TreeNode(nums[0])
        
    que: deque[TreeNode|None] = deque()
    que.append(root)
    
    i: int = 1
    n:int = len(nums)
    
    while i < n and que:
        curr: TreeNode|None = que.popleft()
        if not curr:
            continue

        if i < n and nums[i] != None:
            curr.left = TreeNode(nums[i]) # type:ignore
            i += 1
            que.append(curr.left)
        else:
            i += 1

        if i < n and nums[i] != None:
            curr.right = TreeNode(nums[i]) # type:ignore
            i += 1
            que.append(curr.right)
        else:
            i += 1

    return root


def case1(sol: Solution) -> None:
    root = build_tree([6,2,8,0,4,7,9,None,None,3,5])
    
    result = sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(8))
    if result:
        print(f"case 1 LCA: {result.val}")


def case2(sol: Solution) -> None:
    root = build_tree([6,2,8,0,4,7,9,None,None,3,5])
    
    result = sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(4))
    if result:
        print(f"case 2 LCA: {result.val}")


def main() -> None:
    print("235. Lowest Common Ancestor of a Binary Search Tree")
    sol = Solution()

    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()