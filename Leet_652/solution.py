# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int ):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right:TreeNode|None = None
    
    def __str__(self) -> str:
        return f"{self.val}"

class Solution:
    """
    Given the root of a binary tree, return all duplicate subtrees.

    For each kind of duplicate subtrees, you only need to return the root node of any one of them.

    Two trees are duplicate if they have the same structure with the same node values.
    
    Example1:
        Input: root = [1,2,3,4,null,2,4,null,null,4]

        Output: [[2,4],[4]]

    Example2:
        Input: root = [2,1,1]

        Output: [[1]]
    """ 
    def print_tree(self, root: TreeNode|None) -> None:
        if root == None:
            return
        
        print(root, end=",")
        
        #-- recursion
        self.print_tree(root.left)
        self.print_tree(root.right)
        #--
        
        print("")

    def serialize_key(self, root: TreeNode|None, result: list[str]) -> None:
        if root == None:
            return
        
        result.append(f"({str(root.val)}")
        #-- recursion
        self.serialize_key(root.left, result)
        result.append(")")
        self.serialize_key(root.right, result)
        #--


    def get_duplicate_subtrees(self, root: TreeNode|None, table: dict[str, int], result: list[TreeNode|None]):
        if root == None:
            return

        strs: list[str] = []
        self.serialize_key(root, strs)
        key: str = "".join(strs)
        print(key)
        if key in table:
            table[key] += 1
            if table[key] == 2:
                result.append(root)
        else:
            table[key] = 1

        #-- recursion
        self.get_duplicate_subtrees(root.left, table, result)
        self.get_duplicate_subtrees(root.right, table, result)
        #--

    def find_duplicate_subtrees(self, root: TreeNode|None) -> list[TreeNode|None]:
        table: dict[str, int] = {}
        result: list[TreeNode|None] = []

        self.get_duplicate_subtrees(root, table, result)

        return result



def tree_a() -> None:
    # [1,2,3,4,null,2,4,null,null,4]
    # expected: [[2,4], [4]]
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.right.left = TreeNode(2)
    head.right.right = TreeNode(4)
    head.right.left.left = TreeNode(4)
    
    solution = Solution()
    result = solution.find_duplicate_subtrees(head)
    for r in result:
        solution.print_tree(r)


def tree_b() -> None:
    # [2,1,1]
    # expected: [[1]]
    head = TreeNode(2)
    head.left = TreeNode(1)
    head.right = TreeNode(1)

    solution = Solution()
    result = solution.find_duplicate_subtrees(head)
    for r in result:
        solution.print_tree(r)


def tree_c() -> None:
    # [2,2,2,3,null,3,null]
    # expected: [[2,3],[3]]
    head = TreeNode(2)

    head.left = TreeNode(2)
    head.right = TreeNode(2)

    head.left.left = TreeNode(3)
    head.right.left = TreeNode(3)

    solution = Solution()
    result = solution.find_duplicate_subtrees(head)
    for r in result:
        solution.print_tree(r)


def tree_d() -> None:
    # [0,0,0,0,null,null,0,null,null,null,0]
    # expected: [[0]]
    head = TreeNode(0)
    head.left = TreeNode(0)
    head.right = TreeNode(0)

    head.left.left = TreeNode(0)
    head.right.right = TreeNode(0)
    head.right.right.right = TreeNode(0)

    solution = Solution()
    result = solution.find_duplicate_subtrees(head)
    for r in result:
        solution.print_tree(r)


def main() -> None:
    tree_a()
    print("_______________")

    tree_b()
    print("_______________")

    tree_c()
    print("_______________")

    tree_d()
    print("_______________")

if __name__ == "__main__":
    main()