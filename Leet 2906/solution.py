class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        rows: int = len(grid)
        cols: int = len(grid[0])
        result: list[list[int]] = [[0]*cols for _ in range(rows)]

        suffix: int = 1
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                result[i][j] = suffix
                suffix = (suffix * grid[i][j]) % 12345

        prefix: int = 1
        for i in range(rows):
            for j in range(cols):
                result[i][j] = (prefix * result[i][j]) % 12345
                prefix = (prefix * grid[i][j]) % 12345
        
        return result


def main() -> None:
    print('2906. Construct Product Matrix')

    sol = Solution()
    case1: list[list[int]] = [[1,2], [3,4]]
    
    for row in sol.constructProductMatrix(case1):
        print('[', end='')
        for i, val in enumerate(row):
            if i >= len(row) - 1:
                print(f' {val} ', end='')
            else:
                print(f' {val}, ', end='')
        print(']')


if __name__ == '__main__':
    main()