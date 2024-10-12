class Solution:
    def print_matrix(self, matrix: list[list[int]]) -> None:
        m: int = len(matrix)
        n: int = len(matrix[0])
        for r in range(m):
            print("",end="")
            for c in range(n):
                print(f" {matrix[r][c]:02d} ", end="")
            print("")

    def _set_row(self, matrix: list[list[int]], row: int, value: int) -> None:
        if row < 0 or row > len(matrix) - 1:
            return
            
        n: int = len(matrix[0])
        for col in range(n):
            if matrix[row][col] != value:
                matrix[row][col] = value

    def _set_col(self, matrix: list[list[int]], col: int, value: int) -> None:
        if col < 0 or col > len(matrix[0]) - 1:
            return
            
        m: int = len(matrix)
        for row in range(m):
            if matrix[row][col] != value:
                matrix[row][col] = value

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m: int = len(matrix)
        n: int = len(matrix[0])

        rows: set[int] = set()
        cols: set[int] = set()
            
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r not in rows:
                        rows.add(r)
                    if c not in cols:
                        cols.add(c)

        for r in rows:
            self._set_row(matrix, r, 0)

        for c in cols:
            self._set_col(matrix, c, 0)

        
def case1(sol: Solution) -> None:
    print("case 1")
    matrix: list[list[int]] = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
    sol.print_matrix(matrix)


def case2(sol: Solution) -> None:
    print("case 2")
    matrix: list[list[int]] = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(matrix)
    sol.print_matrix(matrix)


def main() -> None:
    print("73. Set Matrix Zeroes")
    
    sol = Solution()

    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()

