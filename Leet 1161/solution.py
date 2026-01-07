from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def maxLevelSum(self, root: TreeNode|None) -> int:
        if not root:
            return 0
        
        que = deque([root])
        result: int = 0
        max_sum: float = -float('inf')
        current_level: int = 1

        while que:
            count: int = len(que)
            current_sum: int = 0
            for _ in range(count):
                current = que.popleft()
                current_sum += current.val

                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)

            if current_sum > max_sum:
                max_sum = current_sum
                result = current_level
            current_level += 1

        return result


def case1(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    level: int = sol.maxLevelSum(root)
    print(f'case 1 { 'pass' if level == 2 else 'fail' }')


def case2(sol: Solution) -> None:
    root = TreeNode(989)
    root.right = TreeNode(10250)
    root.right.left = TreeNode(98693)
    root.right.right = TreeNode(-89388)
    root.right.right.right = TreeNode(-32127)

    level: int = sol.maxLevelSum(root)
    print(f'case 2 { 'pass' if level == 2 else 'fail' }')


def case3(sol: Solution) -> None:
    root = TreeNode(-100)
    root.left = TreeNode(-200)
    root.right = TreeNode(-300)
    root.left.left = TreeNode(-20)
    root.left.right = TreeNode(-5)
    root.right.left = TreeNode(-10)

    level: int = sol.maxLevelSum(root)
    print(f'case 3 { 'pass' if level == 3 else 'fail' }')


def main() -> None:
    print('1161. Maximum Level Sum of a Binary Tree')

    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == '__main__':
    main()
