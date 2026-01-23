from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def levelOrderBottom(self, root: TreeNode|None) -> list[list[int]]:
        if not root:
            return []

        result: list[list[int]] = []
        que: deque[TreeNode] = deque([root])

        while que:
            count = len(que)
            row: list[int] = []
            for _ in range(count):
                current = que.popleft()
                
                row.append(current.val)

                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)

            if row:
                result.insert(0, row[:])

        return result


def main() -> None:
    print('107. Binary Tree Level Order Traversal II')

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    
    result: list[list[int]] = solution.levelOrderBottom(root)
    print(result)


if __name__ == '__main__':
    main()