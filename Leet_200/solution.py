class Solution:
    # def explored(self, r: int, c: int, row: int, col: int, grid: list[list[str]], explored: list[bool]):
    #     if (r >= 0 and r < row) and (c >= 0 and c < col):
    #         if grid[r][c] == "1" and not explored[r * col + c]:
    #             explored[r * col + c] = True
    #             self.explored(r, c-1, row, col, grid, explored)
    #             self.explored(r, c+1, row, col, grid, explored)
    #             self.explored(r-1, c, row, col, grid, explored)
    #             self.explored(r+1, c, row, col, grid, explored)
            
    #             return True
            
    #     return False
    
    # def numIslands1(self, grid: list[list[str]]) -> int:
    #     row: int = len(grid)
    #     col: int = len(grid[0])
    #     explored: list[bool] = [False] * (row*col)
    #     count: int = 0

    #     for r in range(row):
    #         for c in range(col):
    #             if self.explored(r, c, row, col, grid, explored):
    #                 count += 1

    #     return count

    def numIslands(self, grid: list[list[str]]) -> int:
        row: int = len(grid)
        col: int = len(grid[0])
        stk: list[tuple[int, int]] = []
        capacity: int = (row * col) + 1
        explored: list[bool] = [False] * capacity
        count: int = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and not explored[r * col + c]:

                    stk.append((r, c))

                    while stk:
                        coord: tuple[int, int] = stk.pop()

                        x: int = coord[0]
                        y: int = coord[1]

                        if (x >= 0 and x < row) and (y >= 0 and y < col):
                            if grid[x][y] == "1" and not explored[x * col + y]:
                                explored[x * col + y] = True

                                stk.append((x, y-1))
                                stk.append((x, y+1))
                                stk.append((x+1, y))
                                stk.append((x-1, y))
               
                    count += 1

        return count


def test_1(solution: Solution) -> None:
    print(f"Test 1")

    grid: list[list[str]] = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected: int = 1
    result: int = solution.numIslands(grid)
    print(f"Expected: {expected}")
    print(f"Output: {result}")
    print("")


def test_2(solution: Solution) -> None:
    print(f"Test 2")

    grid: list[list[str]] = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected: int = 3
    result: int = solution.numIslands(grid)
    print(f"Expected: {expected}")
    print(f"Output: {result}")
    print("")


def test_3(solution: Solution) -> None:
    print(f"Test 3")

    grid: list[list[str]] = [["1","0","1","1","0","1","1"]]
    expected: int = 3
    result: int = solution.numIslands(grid)
    print(f"Expected: {expected}")
    print(f"Output: {result}")
    print("")


def test_4(solution: Solution) -> None:
    print(f"Test 4")

    grid: list[list[str]] = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
    ]
    expected: int = 1
    result: int = solution.numIslands(grid)
    print(f"Expected: {expected}")
    print(f"Output: {result}")
    print("")


def test_5(solution: Solution) -> None:
    print(f"Test 5")

    grid: list[list[str]] = [["1"],["1"]]
    expected: int = 1
    result: int = solution.numIslands(grid)
    print(f"Expected: {expected}")
    print(f"Output: {result}")
    print("")


def main() -> None:
    solution = Solution()
    test_1(solution)
    test_2(solution)
    test_3(solution)
    test_4(solution)
    test_5(solution)

if __name__ == "__main__":
    main()

        