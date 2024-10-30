from collections import deque


class TreeNode:
    def __init__(self, value: int):
        self.val: int = value
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Codec:
    """Used to serialize and deserialize TreeNode structures
    """
    def serialize(self, root: TreeNode|None) -> str:
        """Encodes a tree to a single string.
        
        Args:
            root: A TreeNode structure that can be serialized or None

        Returns:
            A string representation of a TreeNode structure

        Example:
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> codec = Codec()
        >>> print(codec.serialize(root))
        """
        if root == None:
            return ""

        nodes: list[str] = []
        str_builder: list[str] = [f"{root.val}"]

        que: deque[TreeNode|None] = deque()
        que.append(root)
        while que:
            
            n: int = len(que)

            for _ in range(n):
                current: TreeNode|None = que.popleft()

                if current == None:
                    continue
                
                if current.left != None:
                    que.append(current.left)
                    nodes.append(f"{current.left.val}")
                else:
                    nodes.append("null")
                
                if current.right != None:
                    que.append(current.right)
                    nodes.append(f"{current.right.val}")
                else:
                    nodes.append("null")

            # update str builder
            if len(nodes) > 0:
                for node in nodes:
                    str_builder.append(node)
                nodes.clear()

        # simple workaround to remove trailing nulls
        n: int = len(str_builder)
        count: int = 0
        for sb in reversed(str_builder):
            if sb != "null":
                break
            count += 1

        return ",".join(str_builder[: (n - count)])
        

    def deserialize(self, data: str) -> TreeNode|None:
        """Decodes your encoded data to tree.
        
        Args:
            data: A serialized treenode structure that can be deserialized

        Returns:
            A TreeNode structure or None

        Example:
        >>> codec = Codec()
        >>> root: TreeNode|None = codec.deserialize("1,2,3")
        """

        if len(data) == 0:
            return None
        
        values: list[str] = data.split(",")
        if values[0] == "null":
            return None
        
        root: TreeNode|None = TreeNode(int(values[0]))
        que: deque[TreeNode|None] = deque()
        que.append(root)

        i: int = 1
        
        # build tree
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


def _print_treenode_in_preorder(root: TreeNode|None) -> None:
    """Helper recursive function for print_treenode_in_preorder
    """
    if root == None:
        return
    
    print(f" {root.val} ", end="")
    _print_treenode_in_preorder(root.left)
    _print_treenode_in_preorder(root.right)


def print_treenode_in_preorder(root: TreeNode|None, msg: str|None = None) -> None:
    """Print TreeNode structure

    Args:
        root: TreeNode to print
        msg: message that is displayed before printing TreeNode if not None
    """
    if root == None:
        return
    
    if msg == None:
        print(f"[", end="")
    else:
        print(f"{msg}: [", end="")
    _print_treenode_in_preorder(root)
    print("]")


def case1(codec: Codec) -> None:
    """Test case 1
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # TEST
    print_treenode_in_preorder(root, "case 1 tree")

    serialize: str = codec.serialize(root)
    print(f"case 1 serialized: {serialize}")

    deserialize: TreeNode|None = codec.deserialize(serialize)
    print_treenode_in_preorder(deserialize, "case 1 deserialized")


def case2(codec: Codec) -> None:
    """Test case 2
    """
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    root.right.left.left = TreeNode(6)
    root.right.right.left = TreeNode(7)

    # TEST
    print_treenode_in_preorder(root, "case 2 tree")

    serialize: str = codec.serialize(root)
    print(f"case 2 serialized: {serialize}")

    deserialize: TreeNode|None = codec.deserialize(serialize)
    print_treenode_in_preorder(deserialize, "case 2 deserialized")



def main() -> None:
    print("297. Serialize and Deserialize Binary Tree")

    codec = Codec()
    
    case1(codec)
    case2(codec)


if __name__ == "__main__":
    main()