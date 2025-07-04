class Solution:
    """
    498. Diagonal Traverse:

    Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
    
    Example:
        
        Input: mat = [[1,2,3],[4,5,6],[7,8,9]]

        Output: [1,2,4,7,5,3,6,8,9]
    """
    def clamp(self, val: int, lo: int, hi: int):
        """ Clamp value between hi and lo
        """
        if val <= lo: 
            return lo
        if val >= hi: 
            return hi
        return val

    def solve_square(self, mat:list[list[int]], n: int) -> list[int]:
        """ Solve for a square matrix

        for example a 3x3 Matrix
        """
        result: list[int] = []

        for i in range(2 * n - 1):
            start: int = self.clamp(-n + i + 1, 0, n)
            stop: int = self.clamp(i + 1, 0, n)

            if i % 2 == 0:
                for j in range(start, stop):
                    result.append(mat[i-j][j])
            else:
                for j in reversed(range(start, stop)):
                    result.append(mat[i-j][j])

        return result

    def solve_not_square(self, mat: list[list[int]], m: int, n: int) -> list[int]:
        """ Solve for a non square matrix

        for example a 2x3 Matrix
        """
        result: list[int] = []

        for i in range((n+m) - 1):
            start: int = self.clamp(-n + i + 1, 0, m)
            stop: int = self.clamp(i + 1, 0, m)

            if i % 2 == 0:
                for j in range(start, stop):
                    result.append(mat[i-j][j])
            else:
                for j in reversed(range(start, stop)):
                    result.append(mat[i-j][j])

        return result

    def solve_m(self, mat: list[list[int]], n: int) -> list[int]:
        """N = 1 within the m x n matrix
        """
        result: list[int] = []

        for i in range(n):
            result.append(mat[i][0])

        return result

    def solve_n(self, mat: list[list[int]], m: int) -> list[int]:
        """M = 1 within the m x n matrix
        """
        result: list[int] = []

        for i in range(m):
            result.append(mat[0][i])

        return result

    def findDiagonalOrder2(self, mat: list[list[int]]) -> list[int]:
        m: int = len(mat)
        n: int = len(mat[0])

        if m == 1:
            return self.solve_n(mat, n)
        
        if n == 1:
            return self.solve_m(mat, m)
        
        if m != n:
            return self.solve_not_square(mat, n, m)

        return self.solve_square(mat, m)


def main() -> None:
    solution = Solution()
    print(solution.findDiagonalOrder2([[1,2,3],[4,5,6],[7,8,9]]))
    print(solution.findDiagonalOrder2([[1],[2],[3]]))
    print(solution.findDiagonalOrder2([[2,5,8], [4,0,-1]]))
    print(solution.findDiagonalOrder2([[2,5], [4,0], [2,-1]]))
    print(solution.findDiagonalOrder2([[1]]))

if __name__ == "__main__":
    main()