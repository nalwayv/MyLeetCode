from collections import deque


class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def averageOfLevels(self, root: TreeNode|None) -> list[float]:
        result: list[float] = []

        que: deque[TreeNode|None] = deque()
        que.append(root)

        while que:
            n: int = len(que)

            total: float = 0
            tally: int = 0

            for _ in range(n):
                curr: TreeNode|None = que.popleft()
                
                if not curr:
                    continue

                total += curr.val
                tally += 1

                que.append(curr.left)
                que.append(curr.right)

            if tally > 0:
                result.append(total / tally)

        return result


def main() -> None:
    print("637. Average of Levels in Binary Tree")

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    result: list[float] = sol.averageOfLevels(root)

    print("Case 1")
    for level, num in enumerate(result):
        print(f"Level {level} = {num}")


if __name__ == "__main__":
    main()