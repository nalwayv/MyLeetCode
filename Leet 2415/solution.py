from collections import deque


class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _is_even(self, n: int) -> bool:
        return (n ^ 1) == (n + 1)
    
    def reverseOddLevels(self, root: TreeNode|None) -> TreeNode|None:
        """Reverse each odd levels nodes in the tree
        """
        if not root:
            return root
        
        que: deque[TreeNode] = deque()
        que.append(root)
        nodes: list[TreeNode] = []
        level: int = 1

        while que:
            count: int = len(que)
            for _ in range(count):
                curr: TreeNode = que.popleft()

                if curr.left:
                    que.append(curr.left)
                    nodes.append(curr.left)

                if curr.right:
                    que.append(curr.right)
                    nodes.append(curr.right)

            #Reverse level
            n: int = len(nodes)
            if n > 0 and not self._is_even(level):
                p1: int = 0
                p2: int = n - 1
                while p1 < p2:
                    nodes[p1].val, nodes[p2].val = nodes[p2].val, nodes[p1].val
                    p1 += 1
                    p2 -= 1

            if n > 0:
                nodes.clear()

            level += 1

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
    tree: list[int] = [2,3,5,8,13,21,34]
    root = build_tree(tree)
    result = sol.reverseOddLevels(root)
    print_tree_by_level(result)

    print("")


def case2(sol: Solution):
    print("Case 2: ")

    tree: list[int] = [7,13,11]
    root = build_tree(tree)
    result = sol.reverseOddLevels(root)
    print_tree_by_level(result)

    print("")


def case3(sol: Solution):
    print("Case 3: ")

    tree: list[int] = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
    root = build_tree(tree)
    result = sol.reverseOddLevels(root)
    print_tree_by_level(result)

    print("")


def main() -> None:
    print("2415. Reverse Odd Levels of Binary Tree")
    
    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()