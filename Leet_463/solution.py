class Solution:
    def is_land(self, grid: list[list[int]], coord: tuple[int, int]) -> bool:
        return grid[coord[0]][coord[1]] == 1
    
    def is_on_grid(self, grid: list[list[int]], coord: tuple[int, int]) -> bool:
        rows: int = len(grid)
        cols: int = len(grid[0])
        
        check_x: bool = coord[0] >= 0 and coord[0] < rows
        check_y: bool = coord[1] >= 0 and coord[1] < cols

        return check_x and check_y

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

        stk: list[tuple[int, int]] = []
        explored: set[tuple[int, int]] = set()
        directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perimeter: int = 0

        for r in range(rows):
            for c in range(cols):

                coord: tuple[int, int] = (r, c)
                
                if self.is_land(grid, coord) and coord not in explored:
                    stk.append(coord)
                    explored.add(coord)

                    while stk:
                        curr: tuple[int, int] = stk.pop()

                        neighbours: int = 4
                        for dir in directions:
                            neighbour: tuple[int, int] = (curr[0] + dir[0], curr[1] + dir[1])

                            if self.is_on_grid(grid, neighbour) and self.is_land(grid, neighbour):
                                neighbours -= 1

                                if neighbour not in explored:
                                    stk.append(neighbour)
                                    explored.add(neighbour)

                        perimeter += neighbours


        return perimeter


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