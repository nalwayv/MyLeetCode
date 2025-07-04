class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _frequency(self, root: TreeNode|None, mode: dict[int, int]) -> None:
        if not root:
            return

        if root.val in mode:
            mode[root.val] += 1
        else:
            mode[root.val] = 1

        self._frequency(root.left, mode)
        self._frequency(root.right, mode)

    def findMode(self, root: TreeNode|None) -> list[int]:
        table: dict[int, int] = {}
        self._frequency(root, table)

        result: list[int] = []
        max_val: int = 0

        # collect all keys with same max frequency
        for key,val in table.items():
            if val > max_val:
                max_val = val
                result.clear()
                result.append(key)
            elif val == max_val:
                result.append(key)

        return result


def case1(sol: Solution) -> None:
    print("Case 1")
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    result: list[int] = sol.findMode(root)
    print(f"{"":>2}= {result}")


def case2(sol: Solution) -> None:
    print("Case 2")
    root = TreeNode(0)
    result: list[int] = sol.findMode(root)
    print(f"{"":>2}= {result}")


def case3(sol: Solution) -> None:
    print("Case 3")
    root = TreeNode(1)
    root.left = TreeNode(2)

    result: list[int] = sol.findMode(root)
    print(f"{"":>2}= {result}")


def main() -> None:
    print("501. Find Mode in Binary Search Tree")

    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()