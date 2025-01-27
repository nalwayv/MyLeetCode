class TreeNode:
    def __init__(self, val: int=0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _pre_order_populate_values(self, root: TreeNode|None, values: list[int]) -> None:
        if not root:
            return
        
        values.append(root.val)

        self._pre_order_populate_values(root.left, values)
        self._pre_order_populate_values(root.right, values)

    def _clean(self, root: TreeNode|None) -> None:
        if not root:
            return
        
        if root.left:
            self._clean(root.left)
            root.left = None
        
        if root.right:
            self._clean(root.right)
            root.right = None

    def flatten(self, root: TreeNode|None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        values: list[int] = []
        self._pre_order_populate_values(root, values)
        self._clean(root)

        root.val = values[0]
        stk: list[TreeNode|None] = [root]
        
        i: int = 1
        n: int = len(values)

        while stk:
            curr = stk.pop()

            if not curr:
                continue

            if i < n:
                curr.right = TreeNode(values[i])
                i += 1
                stk.append(curr.right)


def print_binary_tree(root: TreeNode) -> None:
    if not root:
        return
    
    print(f"^: {root.val}")

    stk: list[TreeNode|None] = [root]
    while stk:
        curr: TreeNode|None = stk.pop()
        if not curr:
            continue

        if curr.left:
            print(f"<: {curr.left.val}")

        if curr.right:
            print(f">: {curr.right.val}")

        stk.append(curr.left)
        stk.append(curr.right)


def case1(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    print("Before")
    print_binary_tree(root)
    
    sol.flatten(root)

    print("Flatten")
    print_binary_tree(root)


def main() -> None:
    print("114. Flatten Binary Tree to Linked List")

    sol = Solution()
    case1(sol)


if __name__ == "__main__":
    main()