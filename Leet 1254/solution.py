def grid_is_in_range(grid: list[list[int]], x: int, y: int) -> bool:
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def grid_is_on_edge(grid: list[list[int]], x: int, y: int) -> bool:
    edge_x: bool = x == 0 or x == len(grid) - 1
    edge_y: bool = y == 0 or y == len(grid[0]) - 1
    return edge_x or edge_y


def explore_closed_island(grid: list[list[int]], row: int, col: int, explored: list[bool]) -> bool:
    if not grid_is_in_range(grid, row, col) or grid[row][col] != 0 or explored[row * len(grid[0]) + col]:
        return False

    explored[row * len(grid[0]) + col] = True

    # check if tile that makes up this island does not touch the grid boundary
    # else it should be rejected.
    on_edge: bool = grid_is_on_edge(grid, row, col)

    on_edge = explore_closed_island(grid, row+1, col, explored) or on_edge
    on_edge = explore_closed_island(grid, row-1, col, explored) or on_edge
    on_edge = explore_closed_island(grid, row, col+1, explored) or on_edge
    on_edge = explore_closed_island(grid, row, col-1, explored) or on_edge

    return on_edge


def closed_island(grid: list[list[int]]) -> int:
    rows: int = len(grid)
    cols: int = len(grid[0])

    explored: list[bool] = [False] * (rows * cols)
    
    count: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0 and not explored[row * cols + col]:
                if not explore_closed_island(grid, row, col, explored):
                    count += 1

    return count


def main() -> None:
    print("1254. Number of Closed Islands")

    grid_1: list[list[int]] = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    print(f"Result should equal 2 ? {closed_island(grid_1)}")

    grid_2: list[list[int]] = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
    print(f"Result should equal 1 ? {closed_island(grid_2)}")

    grid_3: list[list[int]] = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    print(f"Result should equal 2 ? {closed_island(grid_3)}")


if __name__ == "__main__":
    main()
