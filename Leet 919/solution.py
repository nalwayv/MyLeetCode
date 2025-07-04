from collections import deque

class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class CBTInserter:
    def __init__(self, root: TreeNode|None):
        self.root = root

    def insert(self, val: int) -> int:
        if not self.root:
            return -1
        
        que: deque[TreeNode|None] = deque([self.root])

        while que:
            n: int = len(que)
            for _ in range(n):
                parent: TreeNode|None = que.popleft()

                if not parent:
                    continue
                
                if parent.left:
                    que.append(parent.left)
                else:
                    parent.left = TreeNode(val)
                    return parent.val

                if parent.right:
                    que.append(parent.right)
                else:
                    parent.right = TreeNode(val)
                    return parent.val
        
        return -1
    
    def get_root(self) -> TreeNode|None:
        return self.root
        

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()


def print_tree(root: TreeNode|None) -> None:
    if not root:
        return
    
    
    print(f"Level 0: [ {root.val} ]")
    
    depth: int = 1
    que: deque[TreeNode|None] = deque([root])

    while que:
        n: int = len(que)
        level: list[int] = []

        for _ in range(n):
            parent: TreeNode|None = que.popleft()

            if not parent:
                continue
            
            if parent.left:
                que.append(parent.left)
                level.append(parent.left.val)

            if parent.right:
                que.append(parent.right)
                level.append(parent.right.val)

        if level:
            print(f"Level {depth}: [", end="")
            for val in level:
                print(f" {val} ", end="")
            print("]")
        depth += 1


def main() -> None:
    print("___ 919. Complete Binary Tree Inserter ___")
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    print("Root: [1, 2]")

    obj = CBTInserter(root)
    print(f"insert(3) Parent = 1 ? {obj.insert(3)}")
    print(f"insert(4) Parent = 2 ? {obj.insert(4)}")

    print("Print Tree:")
    print_tree(obj.get_root())


if __name__ == "__main__":
    main()