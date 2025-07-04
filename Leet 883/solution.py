class Solution:
    def count_z(self, grid: list[list[int]]) -> int:
        count: int = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    count += 1
        
        return count

    def count_x(self, grid: list[list[int]]) -> int:
        count: int = 0

        for line in grid:
            count += max(line)

        return count

    def count_y(self, grid: list[list[int]]) -> int:
        count: int = 0

        for j in range(len(grid[0])):
            current_max: int = 0
            for i in range(len(grid)):
                current_max = max(current_max, grid[i][j])
            count += current_max

        return count

    def projectionArea(self, grid: list[list[int]]) -> int:
        z: int = self.count_z(grid)
        x: int = self.count_x(grid)
        y: int = self.count_y(grid)

        return z + x + y


def test_case_1(sol: Solution) -> None:
    grid: list[list[int]] = [[1,2], [3,4]]
    result: str = "pass" if sol.projectionArea(grid) == 17 else "fail"
    print(f"Case 1 {grid} should equil 17: {result}")


def main() -> None:
    print("883. Projection Area of 3D Shapes")

    sol = Solution()
    test_case_1(sol)


if __name__ == "__main__":
    main()