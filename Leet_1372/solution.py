from collections import deque
from enum import Enum


class Direction(Enum):
    Left = 1
    Right = 2


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def longestZigZag(self, root: TreeNode|None) -> int:
        if not root:
            return 0

        max_zz: int = 0

        stk: deque[tuple[TreeNode|None, Direction, int]] = deque()
        stk.append((root, Direction.Left, 0))
        while stk:
            curr, dir, count = stk.pop()
            
            if not curr:
                continue
            
            max_zz = max(max_zz, count)

            if dir == Direction.Left:
                stk.append((curr.left, Direction.Left, 1))
                stk.append((curr.right, Direction.Right, 1 + count))
            else:
                stk.append((curr.left, Direction.Left, 1 + count))
                stk.append((curr.right, Direction.Right, 1))

        return max_zz 
    

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


def case1(sol: Solution):
    tree: list[int|None] = [1,None,2,3,4,None,None,5,6,None,7,None,None,None,8]
    root = build_tree(tree)
    result: bool = sol.longestZigZag(root) == 3
    print(f"Case 1 { "pass" if result else "fail" }")


def case2(sol: Solution):
    tree: list[int|None] = [1,1,1,None,1,None,None,1,1,None,1]
    root = build_tree(tree)
    result: bool = sol.longestZigZag(root) == 4
    print(f"Case 2 { "pass" if result else "fail" }")


def case3(sol: Solution):
    tree: list[int|None] = [1]
    root = build_tree(tree)
    result: bool = sol.longestZigZag(root) == 0
    print(f"Case 3 { "pass" if result else "fail" }")


def main() -> None:
    print("1372. Longest ZigZag Path in a Binary Tree")
    
    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()