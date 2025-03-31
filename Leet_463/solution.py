class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """ Given a row x col gridou are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water
        and with exacly one island on the map itself return the permneter of that island

        Args:
            grid (list[list[int]]): row x col grid that has exactly one island on it

        Returns:
            int: perimeter of the island on the grid
        """
        rows: int = len(grid)
        cols: int = len(grid[0])
        result: int = 0

        for r in range(rows):
            for c in range(cols):
        
                if grid[r][c] == 1:
        
                    perimeter: int = 4
                    for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        r2: int = r + dir[0]
                        c2: int = c + dir[1]
                        if (r2 >= 0 and r2 < rows and c2 >= 0 and c2 < cols) and (grid[r2][c2] == 1):
                            perimeter -= 1
        
                    result += perimeter

        return result


def case_1(sol: Solution) -> None:
    grid: list[list[int]] = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0],
    ]
    result: int = sol.islandPerimeter(grid)
    print(f"Case 1: {result}")


def case_2(sol: Solution) -> None:
    grid: list[list[int]] = [[1]]
    result: int = sol.islandPerimeter(grid)
    print(f"Case 2: {result}")


def case_3(sol: Solution) -> None:
    grid: list[list[int]] = [[1,0]]
    result: int = sol.islandPerimeter(grid)
    print(f"Case 3: {result}")


def main() -> None:
    print("463. Island Perimeter")

    sol = Solution()
    
    case_1(sol)
    case_2(sol)
    case_3(sol)


if __name__ == "__main__":
    main()