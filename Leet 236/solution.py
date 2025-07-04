from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _dfs(self, root: TreeNode|None, a: TreeNode, b: TreeNode) -> TreeNode|None:
        if not root:
            return None
        
        if root.val == a.val or root.val == b.val:
            return root

        left = self._dfs(root.left, a, b)
        right = self._dfs(root.right, a, b)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right

        return None

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
    tree: list[int|None] = [1,2,3,4,5,6,7,8,9,10,20,None,None,None,None,None,None,None,None,11,30]
    root: TreeNode|None = build_tree(tree)
    result: TreeNode|None = sol.lowestCommonAncestor(root, TreeNode(8), TreeNode(11))
    if result:
        print(f"LCA({result.val}) == 2")
        print(f"case 1 { "pass" if result.val == 2 else "fail" }")
    else:
        print("fail")


def main() -> None:
    print("236. Lowest Common Ancestor of a Binary Tree")
    sol = Solution()
    case1(sol)


if __name__ == "__main__":
    main()