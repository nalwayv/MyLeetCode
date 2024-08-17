from collections import deque


class TreeNode:
    def __init__(self, val:int = 0):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def rightSideView(self, root: TreeNode|None) -> list[int]:
        def get_right_side_view_values(root: TreeNode|None) -> list[int]:
            """collect all right most values in view
            """
            # depth | vals
            # ------+-----
            # 0     | [1]
            # 1     | [2,3]
            # 2     | [5,4]
            #
            # result [1,3,4]

            result: list[int] = []

            if root == None:
                return result
            
            result.append(root.val)

            que: deque[TreeNode|None] = deque()
            que.append(root)
            
            while que:
                # save current level values into list
                # then get last one as that happens to be the right most in view
                current_level: list[int] = []
                
                for _ in range(len(que)):
                    current: TreeNode|None = que.popleft()
                    if current == None:
                        continue
                    
                    if current.left != None:
                        que.append(current.left)
                        current_level.append(current.left.val)
                        
                    if current.right != None:
                        que.append(current.right)
                        current_level.append(current.right.val)
                
                if len(current_level) > 0:   
                    result.append(current_level[-1])

            return result

        return get_right_side_view_values(root)


def case1(sol: Solution):
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c
    b.right = e
    c.right = d
    
    print(sol.rightSideView(a))


def case2(sol: Solution):
    a = TreeNode(1)
    b = TreeNode(3)

    a.right = b
    
    print(sol.rightSideView(a))


def case3(sol: Solution):
    print(sol.rightSideView(None))


def case4(sol: Solution):
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)

    a.left = b
    a.right = c
    b.right = d

    print(sol.rightSideView(a))


def case5(sol: Solution):
    a = TreeNode(1)
    b = TreeNode(2)

    a.left = b

    print(sol.rightSideView(a))


def main():
    print("199. Binary Tree Right Side View")

    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)
    case5(sol)


if __name__ == "__main__":
    main()