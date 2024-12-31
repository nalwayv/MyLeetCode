class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    # Recursive 
    
    def _get_paths(self, root: TreeNode|None, depth: int, path: list[int], paths: list[str]) -> None:
        if not root:
            return
        
        if depth < len(path):
            path[depth] = root.val
        else:
            path.append(root.val)

        depth += 1

        if not root.left and not root.right:
            str_builder: list[str] = []
            for i in range(depth):
                str_builder.append(str(path[i]))

            new_path: str = "->".join(str_builder)
            paths.append(new_path)    
        else:
            self._get_paths(root.left, depth, path, paths)
            self._get_paths(root.right, depth, path, paths)

    def binaryTreePaths(self, root: TreeNode|None) -> list[str]:
        """Given the root of a binary tree, return a list of all root to leaf paths in any order.
        """
        path: list[int] = []
        paths: list[str] = []
        self._get_paths(root, 0, path, paths)
        return paths

    # Non Recursive
    
    def binaryTreePaths2(self, root: TreeNode|None) -> list[str]:
        """Given the root of a binary tree, return a list of all root to leaf paths in any order.
        """
        path: list[int] = []
        paths: list[str] = []

        stk: list[tuple[TreeNode|None, int]] = [(root, 0)]

        while stk:
            current, depth = stk.pop()
            if not current:
                continue

            if depth < len(path):
                path[depth] = current.val
            else:
                path.append(current.val)

            if not current.left and not current.right:
                str_builder: list[str] = []
                for i in range(depth + 1):
                    str_builder.append(str(path[i]))

                new_path: str = "->".join(str_builder)
                paths.append(new_path)
            else:
                stk.append((current.left, depth + 1))
                stk.append((current.right, depth + 1))

        return paths


def case1(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    paths: list[str] = sol.binaryTreePaths2(root)

    print("Case 1")
    for path in paths:
        print(f"{"":>2}{path}")


def case2(sol: Solution) -> None:
    root = TreeNode(1)

    paths: list[str] = sol.binaryTreePaths2(root)

    print("Case 2")
    for path in paths:
        print(f"{"":>2}{path}")


def case3(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.left.right.left.left = TreeNode(9)
    root.left.right.left.right = TreeNode(10)

    paths: list[str] = sol.binaryTreePaths2(root)

    print("Case 3")
    for path in paths:
        print(f"{"":>2}{path}")


def case4(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)

    paths: list[str] = sol.binaryTreePaths2(root)

    print("Case 4")
    for path in paths:
        print(f"{"":>2}{path}")


def main() -> None:
    print("257. Binary Tree Paths")

    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)


if __name__ == "__main__":
    main()