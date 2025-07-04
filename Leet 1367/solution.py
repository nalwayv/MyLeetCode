class ListNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.next: ListNode|None = None


class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def _contains_listnode(self, list_a: list[int], head: ListNode|None):
        """check if listnode can be found within list_a"""
        if not head:
            return
        
        n: int = len(list_a)
        p1: int = 0
        end: int = n - 1
        while p1 < end:
            p2: int = p1

            while p2 < end and list_a[p2] != head.val:
                p2 += 1
        
            if list_a[p2] == head.val:
                i: int = 0
                ok: bool = True
                current: ListNode|None = head

                while current:
                    if p2 + i > end or current.val != list_a[p2 + i]:
                        ok = False
                        break

                    current = current.next
                    i += 1

                if ok:
                    return True

            p1 = p2+1

        return False

    def _populate_paths_with_treenode_paths(self, root: TreeNode|None, current: list[int], paths: list[list[int]], i: int = 0):
        if not root:
            return
        
        if len(current) > i:
            current[i] = root.val
        else:
            current.append(root.val)

        i += 1

        if not root.left and not root.right:
            cpy: list[int] = [c for c in current]
            paths.append(cpy)
        else:
            self._populate_paths_with_treenode_paths(root.left, current, paths, i)
            self._populate_paths_with_treenode_paths(root.right, current, paths, i)

    # def _does_any_path_contain_listnode(self, root: TreeNode|None, head: ListNode|None, current: list[int], i: int = 0) -> bool:
    #     if not root:
    #         return False
        
    #     if len(current) > i:
    #         current[i] = root.val
    #     else:
    #         current.append(root.val)

    #     i += 1

    #     if not root.left and not root.right:
    #         if self._contains_listnode(current, head):
    #             return True
                    
    #     return (self._does_any_path_contain_listnode(root.left,head, current, i) or 
    #             self._does_any_path_contain_listnode(root.right,head, current, i))

    def isSubPath(self, head: ListNode|None, root: TreeNode|None) -> bool:
        current: list[int] = []
        paths: list[list[int]] = []
        self._populate_paths_with_treenode_paths(root, current, paths)

        for path in paths:
            if self._contains_listnode(path, head): 
                return True
        return False

        # current: list[int] = []
        # return self._does_any_path_contain_listnode(root, head, current)
        

def create_ll(values: list[int]) -> ListNode|None:
    head: ListNode|None = None
    tail: ListNode|None = None
    for value in values:
        if not head:
            head = ListNode(value)
            tail = head
        elif tail:
            tail.next = ListNode(value)
            tail = tail.next
    return head


def case_1(sol: Solution) -> None:
    values: list[int] = [4,2,8]
    head: ListNode|None = create_ll(values)

    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(4)
    d = TreeNode(2)
    e = TreeNode(2)
    f = TreeNode(1)
    g = TreeNode(6)
    h = TreeNode(8)
    i = TreeNode(1)
    j = TreeNode(3)

    a.left = b
    a.right = c
    b.right = d
    c.left = e
    d.left = f
    e.left = g
    e.right = h
    h.left = i
    h.right = j

    print(f"case 1 {'pass' if sol.isSubPath(head, a) else 'fail'}")


def case_2(sol: Solution) -> None:
    values: list[int] = [1,4,2,6]
    head: ListNode|None = create_ll(values)

    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(4)
    d = TreeNode(2)
    e = TreeNode(2)
    f = TreeNode(1)
    g = TreeNode(6)
    h = TreeNode(8)
    i = TreeNode(1)
    j = TreeNode(3)

    a.left = b
    a.right = c
    b.right = d
    c.left = e
    d.left = f
    e.left = g
    e.right = h
    h.left = i
    h.right = j

    print(f"case 2 {'pass' if sol.isSubPath(head, a) else 'fail'}")


def case_3(sol: Solution) -> None:
    values: list[int] = [1,4,2,6,8]
    head: ListNode|None = create_ll(values)

    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(4)
    d = TreeNode(2)
    e = TreeNode(2)
    f = TreeNode(1)
    g = TreeNode(6)
    h = TreeNode(8)
    i = TreeNode(1)
    j = TreeNode(3)

    a.left = b
    a.right = c
    b.right = d
    c.left = e
    d.left = f
    e.left = g
    e.right = h
    h.left = i
    h.right = j

    print(f"case 3 {'pass' if not sol.isSubPath(head, a) else 'fail'}")


def main() -> None:
    print("1367. Linked List in Binary Tree")

    sol = Solution()
    
    case_1(sol)
    case_2(sol)
    case_3(sol)

if __name__ == "__main__":
    main()