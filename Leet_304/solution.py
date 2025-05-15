class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.rows: int = len(matrix)
        self.cols: int = len(matrix[0])

        # build prefix from columns
        self.prefix: list[list[int]] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for j in range(self.cols):
            self.prefix[0][j] = matrix[0][j]
            for i in range(1, self.rows):
                self.prefix[i][j] = self.prefix[i-1][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top: int = row1
        bottom: int = row2
        result: int = 0

        # prefix sum = right - (left-1) if left != 0 else right
        # adding all prefix range sums from each column
        
        for i in range(col1, col2+1):
            if top != 0:
                result += self.prefix[bottom][i] - self.prefix[top-1][i]
            else:
                result += self.prefix[bottom][i]

        return result


def main() -> None:
    print("304. Range Sum Query 2D - Immutable")

    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]

    num_matrix = NumMatrix(matrix)

    print(f"Case 1 should equal 8 ? { "pass" if num_matrix.sumRegion(2,1,4,3) == 8 else "fail" }")
    print(f"Case 2 should equal 11 ? { "pass" if num_matrix.sumRegion(1,1,2,2) == 11 else "fail" }")
    print(f"Case 3 should equal 12 ? { "pass" if num_matrix.sumRegion(1,2,2,4) == 12 else "fail" }")


if __name__ == "__main__":
    main()

