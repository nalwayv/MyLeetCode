class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode|None) -> int:
        """
        """
        count: int = 0

        # tuple ( grandparent, parent, child )
        stk: list[tuple[TreeNode|None, TreeNode|None, TreeNode|None]] = []
        stk.append((None, root, root.left if root else None))
        stk.append((None, root, root.right if root else None))

        while stk:
            grand, parent, child = stk.pop()

            if not grand and not parent and not child:
                continue

            if grand and parent and child:
                # is grandparent even ?
                if grand.val % 2 == 0:
                    count += child.val

            stk.append((parent, child, child.left if child else None))
            stk.append((parent, child, child.right if child else None))

        return count
        

# -- Test Cases


def test_case_1(sol: Solution) -> None:
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)

    print(f"Case 1 should equil 18 ? {'pass' if sol.sumEvenGrandparent(root) == 18 else 'fail'}")


def test_case_2(sol: Solution) -> None:
    root = TreeNode(1)
    print(f"Case 2 should equil 0 ? {'pass' if sol.sumEvenGrandparent(root) == 0 else 'fail'}")


def main() -> None:
    print("1315. Sum of Nodes with Even-Valued Grandparent")

    sol = Solution()
    test_case_1(sol)
    test_case_2(sol)


if __name__ == "__main__":
    main()