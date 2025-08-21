class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        dp: list[list[int]] = [
            [0 for _ in range(cols+1)] 
            for _ in range(rows+1)]
        
        result: int = 0
        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == 1:
                    dp[x + 1][y + 1] = min(dp[x][y+1], dp[x+1][y], dp[x][y]) + 1
                    result += dp[x+1][y+1]

        return result


def main() -> None:
    print("1277. Count Square Submatrices with All Ones")
    
    sol = Solution()

    matrix = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]]
    print(f"case 1 should equal 15 ? {sol.countSquares(matrix)}")

    matrix2 = [
        [1,0,1],
        [1,1,0],
        [1,1,0]]
    print(f"case 2 should equal 7 ? {sol.countSquares(matrix2)}")

    matrix3 = [
        [0,1,1,1],
        [1,1,0,1],
        [1,1,1,1],
        [1,0,1,0]]
    print(f"case 3 should equal 13 ? {sol.countSquares(matrix3)}")


if __name__ == "__main__":
    main()
