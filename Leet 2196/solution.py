class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode|None:
        """
        Constructs a binary tree from a list of descriptions.
        Each description is a list of three integers [parent, child, isLeft], where:
            - parent: the value of the parent node,
            - child: the value of the child node,
            - isLeft: 1 if the child is a left child, 0 if it is a right child.
        The function creates all necessary TreeNode instances, links them according to the descriptions,
        and returns the root of the constructed binary tree.
        
        Args:
            descriptions (list[list[int]]): A list of descriptions, each describing a parent-child relationship.
        
        Returns:
            TreeNode | None: The root node of the constructed binary tree, or None if the input is empty.
        """
        parents: dict[TreeNode, TreeNode] = {}
        table: dict[int, TreeNode] = {}

        for description in descriptions:
            parent, child, left = description

            if parent not in table:
                table[parent] = TreeNode(parent)
            
            if child not in table:
                table[child] = TreeNode(child)

            if left:
                table[parent].left = table[child]
            else:
                table[parent].right = table[child]

            parents[table[child]] = table[parent]

        # find tree root node
        root: TreeNode|None = None
        for node in table.values():
            if node not in parents:
                root = node

        return root


def print_tree(root: TreeNode|None) -> None:
    if not root:
        return
    
    print(f" {root.val} ")
    print_tree(root.left)
    print_tree(root.right)


def main() -> None:
    print("2196. Create Binary Tree From Descriptions")

    sol = Solution()
    
    print("case 1")
    print_tree(sol.createBinaryTree(descriptions=[
        [20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))

    print("case 2")
    print_tree(sol.createBinaryTree(descriptions=[[1,2,1],[2,3,0],[3,4,1]]))
    

if __name__ == "__main__":
    main()