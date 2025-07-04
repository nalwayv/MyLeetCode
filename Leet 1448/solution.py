from collections import deque


class TreeNode:
    def __init__(self, val: int=0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:    
    def goodNodes(self, root: TreeNode|None) -> int:
        if not root:
            return 0
        
        count:int = 0
        stk: list[tuple[TreeNode|None, float]] = [(root, float("-inf"))]
        while stk:
            curr, max_val = stk.pop()
            
            if not curr:
                continue

            if curr.val >= max_val:
                count += 1
                max_val = curr.val

            stk.append((curr.left, max_val))    
            stk.append((curr.right, max_val))    

        return count


def build_tree(nums: list[int|None]) -> TreeNode|None:
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
    root = build_tree([3, 1, 4, 3, None, 1, 5])
    # print_tree(root)
    result: int = sol.goodNodes(root)
    print(f"Case1: {result}")


def case2(sol: Solution) -> None:
    root = build_tree([3, 3, None, 4, 2])
    result: int = sol.goodNodes(root)
    print(f"Case2: {result}")

def case3(sol: Solution) -> None:
    root = build_tree([1])
    result: int = sol.goodNodes(root)
    print(f"Case3: {result}")


def case4(sol: Solution) -> None:
    root = build_tree([0,1,2,3,10,5,9,4,None,None,11,None,6,None,None,None,None,12,None,8,7])
    result: int = sol.goodNodes(root)
    print(f"Case4: {result}")


def main() -> None:
    print("1448. Count Good Nodes in Binary Tree")

    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)


if __name__ == "__main__":
    main()
