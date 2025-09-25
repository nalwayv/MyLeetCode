class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Calculates the minimum path sum from top to bottom in a triangle array.
        Args:
            triangle (list[list[int]]): A list of lists of integers representing the triangle,
                where triangle[i][j] is the value at row i and column j.
        Returns:
            int: The minimum path sum from top to bottom of the triangle.
        The function uses dynamic programming to build a table of minimum sums from the bottom row up.
        At each step, it chooses the minimum path sum from the two adjacent numbers in the row below.
        """
        length: int = len(triangle)
        dp: list[list[int]] = [
            [0 for _ in range(length)]
            for _ in range(length)
        ]

        for i in range(length):
            dp[length - 1][i] = triangle[length - 1][i]

        for i in range(length - 2, -1, -1):
            current_tri: list[int] = triangle[i]
            current_length: int = len(current_tri)
            for j in range(current_length):
                dp[i][j] = current_tri[j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]


def main() -> None:
    print('120 Triangle')

    solution = Solution()

    case1: int = solution.minimumTotal(triangle= [[2],[3,4],[6,5,7],[4,1,8,3]])
    print(f'case 1 {case1}')

    case2: int = solution.minimumTotal(triangle= [[-1],[2,3],[1,-1,-3]])
    print(f'case 2 {case2}')


if __name__ == '__main__':
    main()