from collections import deque


class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def invertTree(self, root: TreeNode|None) -> TreeNode|None:
        if not root:
            return root
        
        que: deque[TreeNode|None] = deque()
        que.append(root)

        while que:
            count: int = len(que)

            for _ in range(count):
                curr: TreeNode|None = que.popleft()
                
                if not curr:
                    continue

                if curr.left:
                    que.append(curr.left)

                if curr.right:
                    que.append(curr.right)

                # Swap
                tmp: TreeNode|None = curr.left
                curr.left = curr.right
                curr.right = tmp

        return root


def build_tree(nums: list[int]) -> TreeNode|None:
    """Build binary tree from list of ints
    """
    if not nums:
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

        if i < n:
            curr.left = TreeNode(nums[i])
            i += 1
            que.append(curr.left)
        else:
            i += 1

        if i < n:
            curr.right = TreeNode(nums[i])
            i += 1
            que.append(curr.right)
        else:
            i += 1

    return root


def print_tree_by_level(root: TreeNode|None) -> None:
    if not root:
        print("[]")
        return
        
    que: deque[TreeNode] = deque()
    que.append(root)
    level: int = 1
    values: list[int] = []

    print(f"0: [ {root.val} ]")
    while que:
        count: int = len(que)
        for _ in range(count):
            curr = que.popleft()

            if curr.left:
                que.append(curr.left)
                values.append(curr.left.val)
            if curr.right:
                que.append(curr.right)
                values.append(curr.right.val)

        if values:
            print(f"{level}: [", end="")
            for val in values:
                print(f" {val} ", end="")
            print("]")

            values.clear()
        
        level += 1


def case1(sol: Solution):
    print("Case 1: ")
    tree: list[int] = [4,2,7,1,3,6,9] # -> [4,7,2,9,6,3,1]
    root = build_tree(tree)
    result = sol.invertTree(root)
    print_tree_by_level(result)

    print("")


def case2(sol: Solution):
    print("Case 2: ")
    tree: list[int] = [2,1,3] # -> [2,3,1]
    root = build_tree(tree)
    result = sol.invertTree(root)
    print_tree_by_level(result)

    print("")


def case3(sol: Solution):
    print("Case 3: ")

    tree: list[int] = [] # -> []
    root = build_tree(tree)
    result = sol.invertTree(root)
    print_tree_by_level(result)

    print("")


def case4(sol: Solution):
    print("Case 4: ")
    
    root = TreeNode(1)
    root.right = TreeNode(2)

    result = sol.invertTree(root)
    print_tree_by_level(result)

    print("")


def main() -> None:
    print("226. Invert Binary Tree")
    
    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)


if __name__ == "__main__":
    main()