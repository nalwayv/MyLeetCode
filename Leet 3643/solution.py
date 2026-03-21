class Solution:
    def reverseSubmatrix(
            self,
            grid: list[list[int]],
            x: int,
            y: int,
            k: int) -> list[list[int]]:

        end_row: int = min(x + k, len(grid))
        end_col: int = min(y + k, len(grid[0]))
        values_plus_coords: list[tuple[int, int, int]] = []

        row: int = x
        for r in reversed(range(x, end_row)):
            for c in range(y, end_col):
                values_plus_coords.append((grid[r][c], row, c))
            row += 1

        for val, new_x, new_y in values_plus_coords:
            grid[new_x][new_y] = val

        return grid


def main() -> None:
    print('3643. Flip Square Submatrix Vertically')

    grid = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]

    sol = Solution()
    new_grid = sol.reverseSubmatrix(grid, 1,0,3)
    for i in range(len(new_grid)):
        print('[',end='')
        for j in range(len(new_grid[0])):
            print(f' {new_grid[i][j]} ',end='')
        print(']')


if __name__ == '__main__':
    main()