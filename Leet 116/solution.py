from collections import deque


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node|None = None
        self.right: Node|None = None

        # used to connect nodes on current level of tree
        self.next: Node|None = None


class Solution:
    def connect(self, root: Node|None) -> Node|None:
        if root == None:
            return root

        que: deque[Node|None] = deque()
        que.append(root)

        level: list[Node] = []

        while que:
            ln: int = len(que)
            
            # populate que and add current children to level
            for _ in range(ln):
                current= que.popleft()

                if current == None:
                    continue

                if current.left != None:
                    que.append(current.left)
                    level.append(current.left)

                if current.right != None:
                    que.append(current.right)
                    level.append(current.right)

            # connect all next pointers on current level
            n: int = len(level)

            if n > 1:
                for i in range(1, n):
                    level[i-1].next = level[i]

            level.clear()

        return root


def print_linked_list(head: Node|None, msg: str) -> None:
    curr = head
    print(f"{msg}: [",end="")
    while curr != None:
        print(f" {curr.val} ",end="")
        curr = curr.next
    print("]")


def case1(sol: Solution) -> None:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol.connect(root)

    # TEST
    print_linked_list(root.left, "case 1 level 2")
    print_linked_list(root.left.left, "case 1 level 3")


def main() -> None:
    print("116. Populating Next Right Pointers in Each Node")

    sol = Solution()
    case1(sol)


if __name__ == "__main__":
    main()