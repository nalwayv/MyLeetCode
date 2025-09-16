from functools import cache


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode|None = None
        self.right: TreeNode|None = None


class Solution:
    @cache # add memoization
    def get_tree(self, n: int) -> list[TreeNode | None]:
        if n % 2 == 0:
            return []
        
        if n == 1:
            return [TreeNode(0)]

        result: list[TreeNode|None] = []
        for i in range(1, n-1, 2):

            left: list[TreeNode|None] = self.get_tree(i)
            right: list[TreeNode|None] = self.get_tree(n - i - 1)

            for l in left:
                for r in right:
                    t = TreeNode(0)
                    t.left = l
                    t.right = r
                    result.append(t)

        return result

    def allPossibleFBT(self, n: int) -> list[TreeNode|None]:
        return self.get_tree(n)
    

def main() -> None:
    print('894. All Possible Full Binary Trees')

    solution = Solution()
    
    i: int = 1
    for tree in solution.allPossibleFBT(n=7):
        print(f'Tree {i}: ', end='')
        stk = [tree]
        while stk:
            curr = stk.pop()
            if not curr:
                print(' - ', end='')
                continue

            print(f' {curr.val} ', end='')
            stk.append(curr.left)
            stk.append(curr.right)

        i += 1
        print()


if __name__ == '__main__':
    main()