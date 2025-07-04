class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    # VERSION  1

    def countNodes(self, root: TreeNode|None) -> int:
        stk: list[TreeNode|None] = [root]
        count: int = 0
        while stk:
            curr = stk.pop()
            if not curr:
                continue

            count += 1
            stk.append(curr.left)
            stk.append(curr.right)
        return count
    
    # VERSION  2

    def _get_count(self, root: TreeNode|None, count: list[int]):
        if not root:
            return
        
        count[0] += 1

        self._get_count(root.left, count)
        self._get_count(root.right, count)

    def countNodes2(self, root: TreeNode|None) -> int:
        count: list[int] = [0]
        self._get_count(root, count)
        return count[0]


def case1(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print(f"Case 1: {sol.countNodes2(root)}")


def case2(sol: Solution) -> None:
    print(f"Case 2: {sol.countNodes2(None)}")


def case3(sol: Solution) -> None:
    root = TreeNode(1)
    print(f"Case 3: {sol.countNodes2(root)}")


def main() -> None:
    print("222. Count Complete Tree Nodes")
    
    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()