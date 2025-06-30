class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        max_rows: dict[int, int] = {}
        max_cols: dict[int, int] = {}

        for r in range(rows):
            for c in range(cols):
                max_rows[r] = max(max_rows.get(r, -1), grid[r][c])
                max_cols[c] = max(max_cols.get(c, -1), grid[r][c])

        result: int = 0
        for r in range(rows):
            for c in range(cols):
                result += abs(grid[r][c] - min(max_rows[r], max_cols[c]))

        return result


def main() -> None:
    print("807. Max Increase to Keep City Skyline")
    
    grid = [[3,0,8,4],
            [2,4,5,7],
            [9,2,6,3],
            [0,3,1,0]]
    
    sol = Solution()
    print(sol.maxIncreaseKeepingSkyline(grid))


if __name__ == "__main__":
    main()
