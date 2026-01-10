class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows: int = len(grid)
        cols: int = len(grid[0])

        across: list[tuple[int, int]] = []
        down: list[tuple[int, int]] = []
        result = [[0 for _ in range(cols)] for _ in range(rows)]

        # count zeros and ones across
        for i in range(rows):
            one: int = 0
            zero: int = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    one += 1
                else:
                    zero += 1
            across.append((one, zero))

        # count zeros and ones down
        for j in range(cols):
            one: int = 0
            zero: int = 0
            for i in range(rows):
                if grid[i][j] == 1:
                    one += 1
                else:
                    zero += 1
            down.append((one, zero))

        for i, a_values in enumerate(across):
            for j, d_values in enumerate(down):
                result[i][j] = a_values[0] + d_values[0] - a_values[1] - d_values[1]
        
        return result
        

def main() -> None:
    print('2482. Difference Between Ones and Zeros in Row and Column')

    solution = Solution()

    case_1 = solution.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]])
    print(case_1)

    case_2 = solution.onesMinusZeros([[1,1,1],[1,1,1]])
    print(case_2)


if __name__ == '__main__':
    main()