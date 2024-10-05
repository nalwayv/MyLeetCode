from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def pathSum(self, root: TreeNode|None, targetSum: int) -> int:
        if not root:
            return 0
    
        count: int = 0

        # simple stack to loop over tree

        stk: list[TreeNode|None] = [root]
        while stk:
            curr = stk.pop()
            if not curr:
                continue

            # inner stack to check current branch for target sum
            # use of tuple to hold that current braches path value

            stk2: list[tuple[TreeNode|None, int]] = [(curr, targetSum - curr.val)]
            while stk2:
                curr2, val = stk2.pop()

                if not curr2:
                    continue
                    
                if val == 0:
                    count += 1

                if curr2.left:
                    stk2.append((curr2.left, val - curr2.left.val))

                if curr2.right:
                    stk2.append((curr2.right, val - curr2.right.val))


            stk.append(curr.left)
            stk.append(curr.right)

        return count
    

def build_tree(nums: list[int|None]) -> TreeNode|None:
    """build tree from list
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
    tree: list[int|None] = [10,5,-3,3,2,None,11,3,-2,None,1]
    root = build_tree(tree)
    test: int = sol.pathSum(root, 8)
    print(f"case1: { "pass" if test else "fail" }")


def case2(sol: Solution) -> None:
    tree: list[int|None] = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    root = build_tree(tree)
    test: int = sol.pathSum(root, 22)
    print(f"case2: { "pass" if test else "fail" }")


def main() -> None:
    print("437. Path Sum III")

    sol = Solution()

    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()