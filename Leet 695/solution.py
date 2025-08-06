class Solution:
    def __init__(self) -> None:
        self.row: int = 0
        self.col: int = 0
        self.area: int = 0
        self.grid: list[list[int]]

    def explore(self, row: int, col: int):
        if row >= 0 and row < self.row and col >= 0 and col < self.col:
            if self.grid[row][col] == 1:
                self.grid[row][col] = 2
                self.area += 1
                self.explore(row + 1, col)
                self.explore(row - 1, col)
                self.explore(row, col + 1)
                self.explore(row, col - 1)

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        self.area = 0

        max_area: int = 0
        for r in range(self.row):
            for c in range(self.col):
                self.explore(r, c)
                max_area = max(max_area, self.area)
                self.area = 0

        return max_area


def main() -> None:
    print("695. Max Area of Island")

    sol = Solution()

    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    case1: int = sol.maxAreaOfIsland(grid1)
    print(case1)

    grid2 = [[0,0,0,0,0,0,0,0]]
    case2: int = sol.maxAreaOfIsland(grid2)
    print(case2)


if __name__ == "__main__":
    main()
