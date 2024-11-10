class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _get_max(self, root: TreeNode|None) -> TreeNode|None:
        if not root:
            return None
        
        while root.right:
            root = root.right

        return root

    def delete_node(self, root: TreeNode|None, value: int) -> TreeNode|None:
        if not root:
            return root
        
        if root.val > value:
            root.left = self.delete_node(root.left, value)

        elif root.val < value:
            root.right = self.delete_node(root.right, value)

        else:
            if root.left and root.right:
                max_node: TreeNode|None = self._get_max(root.left)
                if max_node:
                    root.val = max_node.val
                    root.left = self.delete_node(root.left, root.val)
            else:
                if not root.left:
                    root = root.right

                elif not root.right:
                    root = root.left

        return root


def _print_inorder(r: TreeNode|None):
    if r == None:
        return
    
    _print_inorder(r.left)
    print(f" {r.val} ",end="")
    _print_inorder(r.right)


def print_inorder(root: TreeNode|None):
    print("[",end="")
    _print_inorder(root)
    print("]")


def create_search_tree(values: list[int]):
    def _build(arr: list[int], lo: int, hi: int):
        if lo > hi:
            return None
        
        root: TreeNode|None = None
        mid = (lo + hi) // 2
        root = TreeNode(arr[mid])
        root.left = _build(arr, lo, mid-1)
        root.right = _build(arr, mid+1, hi)
        return root
    
    return _build(values, 0, len(values) - 1)


def main() -> None:
    print("450. Delete Node in a BST")

    root: TreeNode|None = create_search_tree([1,2,3,4,5])

    print("before deleting 4: ",end="")
    print_inorder(root)
    
    sol = Solution()
    root = sol.delete_node(root, 4)
    
    print("after deleting 4: ",end="")
    print_inorder(root)


if __name__ == "__main__":
    main()
    