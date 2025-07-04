class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        rows: int = len(grid)
        cols: int = len(grid[0])
        row2: int = rows - 2
        cols2: int = cols - 2

        result: list[list[int]] = [[0 for _ in range(row2)] for _ in range(cols2)]

        for i in range(row2):
            for j in range(cols2):
                
                max_val: int = -1
                for r in range(i, i + row2):
                    for c in range(j, j + cols2):
                        max_val = max(max_val, grid[r][c])

                result[i][j] = max_val

        return result


def main() -> None:
    print("2373. Largest Local Values in a Matrix")

    sol = Solution()
    grid_1 = [
        [9,9,8,1],
        [5,6,2,6],
        [8,2,6,4],
        [6,2,2,2]]
    print(sol.largestLocal(grid_1))

    grid_2 = [
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,2,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]]
    print(sol.largestLocal(grid_2))
    

if __name__ == "__main__":
    main()