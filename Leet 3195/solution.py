class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        lo_r: int = rows+1
        hi_r: int = 0
        lo_c: int = cols+1
        hi_c: int = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    lo_r = min(lo_r, r)
                    hi_r = max(hi_r, r)
                    lo_c = min(lo_c, c)
                    hi_c = max(hi_c, c)

        return (hi_r - lo_r + 1) * (hi_c - lo_c + 1)


def main() -> None:
    print("3195. Find the Minimum Area to Cover All Ones I")
    sol = Solution()
    grid: list[list[int]] = [
        [0,1,0], 
        [1,0,1]]
    print(sol.minimumArea(grid))
        

if __name__ == "__main__":
    main()