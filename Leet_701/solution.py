from collections import deque

class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


def insert_into_binary_search_tree(root: TreeNode|None, value: int) -> TreeNode|None:
    """Add a value to the binary tree data structure

    Args:
        root (TreeNode|None): add value to this tree
        value (int): value added

    Returns:
        TreeNode with added value
    """
    if root == None:
        return TreeNode(value)
    
    if root.val > value:
        root.left = insert_into_binary_search_tree(root.left, value)
    else:
        root.right = insert_into_binary_search_tree(root.right, value)
    
    return root


def print_binary_tree_depths(root: TreeNode|None) -> None:
    """Print each depths values of root binary tree

    Args:
        root (TreeNode|None) binary tree data structure
    """
    if root == None:
        return
    
    que: deque[TreeNode|None] = deque()
    que.append(root)

    level: list[int] = [root.val]

    print("[",end="")
    while que:
        n: int = len(que)
        for _ in range(n):
            current: TreeNode|None = que.popleft()
            if current == None:
                continue
            
            if current.left != None:
                que.append(current.left)
                level.append(current.left.val)
            
            if current.right != None:
                que.append(current.right)
                level.append(current.right.val)

        if len(level) > 0:
            for value in level:
                print(f" {value} ",end="")
            level.clear()
    print("]")


def deserialize_into_a_binary_tree(data: str) -> TreeNode|None:
    """Decodes a string of int and null values into a binary tree structure.

    Example:
    >>> root =deserialize("1,2,3,null,5")

    Args:
        data (string):
            string of int values to add to tree

    Returns:
        A new TreeNode structure
    """

    if len(data) == 0:
        return None
    
    values: list[str] = data.split(",")
    if values[0] == "null":
        return None
    
    
    root = TreeNode(int(values[0]))
    que: deque[TreeNode|None] = deque()
    que.append(root)

    i: int = 1
    
    while que and i < len(values):
        curr: TreeNode|None = que.popleft()

        if curr == None:
            continue

        if i < len(values) and values[i] != "null":
            curr.left = TreeNode(int(values[i]))
            que.append(curr.left)
            i += 1
        else:
            i += 1

        if i < len(values) and values[i] != "null":
            curr.right = TreeNode(int(values[i]))
            que.append(curr.right)
            i += 1
        else:
            i += 1
            
    return root 


def main() -> None:
    print("701. Insert into a Binary Search Tree")

    root: TreeNode|None = deserialize_into_a_binary_tree("4,2,7,1,3")

    print("before insert: ",end="")
    print_binary_tree_depths(root)

    root = insert_into_binary_search_tree(root, 5)
    
    print("after insert: ",end="")
    print_binary_tree_depths(root)


if __name__ == "__main__":
    main()