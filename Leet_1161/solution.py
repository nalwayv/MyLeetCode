from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    def maxLevelSum(self, root: TreeNode|None) -> int:
        """
        Return level in tree that has the maximum sum
        """
        if root == None:
            return 0
        
        que: deque[TreeNode|None] = deque()
        que.append(root)

        max_sum: int = root.val
        max_level: int = 1

        # start at next level 
        current_level: int = 2
        while que:
            ln: int = len(que)
            
            current_sum: int = 0
            children: int = 0

            # check level and sum up total values
            for _ in range(ln):
                current: TreeNode|None = que.popleft()

                if current == None:
                    continue
                
                if current.left != None:
                    que.append(current.left)
                    current_sum += current.left.val
                    children += 1

                if current.right != None:
                    que.append(current.right)
                    current_sum += current.right.val
                    children += 1
            
            if children > 0 and current_sum > max_sum:
                max_sum = current_sum
                max_level = current_level

            current_level += 1

        return max_level


def case1(sol: Solution) -> None:
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    level: int = sol.maxLevelSum(root)
    print(f"case 1 { "pass" if level == 2 else "fail" }")


def case2(sol: Solution) -> None:
    root = TreeNode(989)
    root.right = TreeNode(10250)
    root.right.left = TreeNode(98693)
    root.right.right = TreeNode(-89388)
    root.right.right.right = TreeNode(-32127)

    level: int = sol.maxLevelSum(root)
    print(f"case 2 { "pass" if level == 2 else "fail" }")


def case3(sol: Solution) -> None:
    root = TreeNode(-100)
    root.left = TreeNode(-200)
    root.right = TreeNode(-300)
    root.left.left = TreeNode(-20)
    root.left.right = TreeNode(-5)
    root.right.left = TreeNode(-10)

    level: int = sol.maxLevelSum(root)
    print(f"case 3 { "pass" if level == 3 else "fail" }")


def main() -> None:
    print("1161. Maximum Level Sum of a Binary Tree")

    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()
