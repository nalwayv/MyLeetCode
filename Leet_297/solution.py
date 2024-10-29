# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/1437460411/
from collections import deque


class TreeNode(object):
    def __init__(self, value: int):
        self.val: int = value
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Codec:
    def _print_pre_order(self, root: TreeNode|None) -> None:
        if root == None:
            return
        
        print(f" {root.val} ", end="")
        self._print_pre_order(root.left)
        self._print_pre_order(root.right)

    def print_pre_order(self, root: TreeNode|None, msg: str) -> None:
        if root == None:
            return
        
        print(f"{msg}: [", end="")
        self._print_pre_order(root)
        print("]")

    def serialize(self, root: TreeNode|None) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
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
        
        :type data: str
        :rtype: TreeNode
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
    

def case1(codec: Codec) -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # TEST
    codec.print_pre_order(root, "case 1 input")

    serialize: str = codec.serialize(root)
    print(f"case 1 serialized: {serialize}")

    deserialize: TreeNode|None = codec.deserialize(serialize)
    codec.print_pre_order(deserialize, "case 1 deserialized")


def case2(codec: Codec) -> None:
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    root.right.left.left = TreeNode(6)
    root.right.right.left = TreeNode(7)

    # TEST
    codec.print_pre_order(root, "case 2 input")

    serialize: str = codec.serialize(root)
    print(f"case 2 serialized: {serialize}")

    deserialize: TreeNode|None = codec.deserialize(serialize)
    codec.print_pre_order(deserialize, "case 2 deserialized")



def main() -> None:
    print("297. Serialize and Deserialize Binary Tree")

    codec = Codec()
    
    case1(codec)
    case2(codec)


if __name__ == "__main__":
    main()