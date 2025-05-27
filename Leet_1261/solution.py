class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class FindElements:
    def __init__(self, root: TreeNode|None):
        self.root = root
        self.values: set[int] = set()
        self.update_root(root)

    def update_root(self, root: TreeNode|None) -> None:
        if not root:
            return

        stk: list[TreeNode|None] = [root]
        root.val = 0
        self.values.add(root.val)

        while stk:
            curr: TreeNode|None = stk.pop()
            if not curr:
                continue

            if curr.left:
                curr.left.val = (curr.val * 2) + 1
                self.values.add(curr.left.val)
                stk.append(curr.left)


            if curr.right:
                curr.right.val = (curr.val * 2) + 2
                self.values.add(curr.right.val)
                stk.append(curr.right)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


def main() -> None:
    print("__ 1261. Find Elements in a Contaminated Binary Tree __")

    root = TreeNode(-1) # 0
    root.left = TreeNode(-1) # 1
    root.right = TreeNode(-1) # 2
    root.left.left = TreeNode(-1)# 3
    root.left.right = TreeNode(-1) # 4
    root.right.right = TreeNode(-1) # 6

    find = FindElements(root)

    print(f"find 1 in updated root? {find.find(1)}")
    print(f"find 6 in updated root? {find.find(6)}")


if __name__ == "__main__":
    main()