class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        rows: int = len(grid)
        cols: int = len(grid[0])
        total: int = 0
        for i in range(rows):
            for j in range(cols):
                total += grid[i][j]

        current_sum: int = 0
        h_total: int = total
        for i in range(rows):
            for j in range(cols):
                current_sum += grid[i][j]
                h_total -= grid[i][j]
            if current_sum == h_total:
                return True
        
        current_sum = 0
        v_total: int = total
        for j in range(cols):
            for i in range(rows):
                current_sum += grid[i][j]
                v_total -= grid[i][j]
            if current_sum == v_total:
                return True

        return False


def main() -> None:
    print('3546. Equal Sum Grid Partition I')
    sol = Solution()
    grid: list[list[int]] = [[1,4],[2,3]]
    test_case1: str = 'pass' if sol.canPartitionGrid(grid) else 'fail'
    print(f'Case 1 {grid} should equal true? {test_case1}')


if __name__ == '__main__':
    main()