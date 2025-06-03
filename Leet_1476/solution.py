class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.matrix: list[list[int]] = rectangle
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def in_range(self, row: int, col: int) -> bool:
        """
        Check if the given row and column indices are within the valid range of the matrix.

        Args:
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if both row and col are within the bounds of the matrix, False otherwise.
        """
        return row >= 0 and row < self.rows and col >= 0 and col < self.cols

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        """
        Updates all values in the subrectangle defined by (row1, col1) to (row2, col2) to newValue.

        Args:
            row1 (int): Starting row index.
            col1 (int): Starting column index.
            row2 (int): Ending row index.
            col2 (int): Ending column index.
            newValue (int): Value to set in the subrectangle.
        """
        if not (self.in_range(row1, col1) and self.in_range(row2, col2)):
            return

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.matrix[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        """
        Returns the value at the specified row and column in the matrix if the indices are within range.

        Args:
            row (int): The row index of the desired value.
            col (int): The column index of the desired value.

        Returns:
            int: The value at matrix[row][col] if the indices are valid; otherwise, -1.
        """
        if self.in_range(row, col):
            return self.matrix[row][col]
        return -1

    def print_matrix(self) -> None:
        for i in range(self.rows):
            print("[",end="")
            for j in range(self.cols):
                print(f" {self.matrix[i][j]} ",end="")
            print("]")


def main() -> None:
    print("--- 1476. Subrectangle Queries ---")
    
    matrix: list[list[int]] = [
        [1,2,1],
        [4,3,4],
        [3,2,1],
        [1,1,1]
    ]

    query = SubrectangleQueries(matrix)
    query.print_matrix()

    print(f"[0,2] = 1 ? {'pass' if query.getValue(0, 2) == 1 else 'fail'}")

    print("updateSubrectangle(0,0,3,2,5)")

    query.updateSubrectangle(0,0,3,2,5)
    query.print_matrix()
    print(f"[0,2] = 5 ? {'pass' if query.getValue(0, 2) == 5 else 'fail'}")
    print(f"[3,1] = 5 ? {'pass' if query.getValue(3, 1) == 5 else 'fail'}")

    print("updateSubrectangle(3, 0, 3, 2, 10)")

    query.updateSubrectangle(3, 0, 3, 2, 10)
    query.print_matrix()
    print(f"[3,1] = 10 ? {'pass' if query.getValue(3, 1) == 10 else 'fail'}")
    print(f"[0,2] = 5 ? {'pass' if query.getValue(0, 2) == 5 else 'fail'}")


if __name__ == "__main__":
    main()