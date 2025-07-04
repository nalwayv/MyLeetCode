class Values:
    def __init__(self) -> None:
        self.adjacent: int = 0
        self.diagonal: int = 0


class NeighborSum:
    def __init__(self, grid: list[list[int]]):
        rows: int = len(grid)
        cols: int = len(grid[0])
        self.values: dict[int, Values] = {}

        for r in range(rows):
            for c in range(cols):
                self.values[grid[r][c]] = Values()
                
                # adjacent
                for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if r + dir[0] >= 0 and r + dir[0] < rows and c + dir[1] >= 0 and c + dir[1] < cols:
                        self.values[grid[r][c]].adjacent += grid[r+dir[0]][c+dir[1]]
                
                # diagonal
                for dir in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    if r + dir[0] >= 0 and r + dir[0] < rows and c + dir[1] >= 0 and c + dir[1] < cols:
                        self.values[grid[r][c]].diagonal += grid[r+dir[0]][c+dir[1]]

    def adjacentSum(self, value: int) -> int:
        if value in self.values:
            return self.values[value].adjacent
        return -1

    def diagonalSum(self, value: int) -> int:
        if value in self.values:
            return self.values[value].diagonal
        return -1


def main() -> None:
    print("3242. Design Neighbor Sum Service")

    grid: list[list[int]] = [
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ]

    neighbor = NeighborSum(grid)

    print(f"adjacentSum(1) = 6 ? {'pass' if neighbor.adjacentSum(1) == 6 else 'fail'}")
    print(f"adjacentSum(4) = 16 ? {'pass' if neighbor.adjacentSum(4) == 16 else 'fail'}")
    print(f"diagonalSum(4) = 16 ? {'pass' if neighbor.adjacentSum(4) == 16 else 'fail'}")
    print(f"diagonalSum(8) = 4 ? {'pass' if neighbor.diagonalSum(8) == 4 else 'fail'}")


if __name__ == "__main__":
    main()