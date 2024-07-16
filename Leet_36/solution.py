class Solution:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.

    Each column must contain the digits 1-9 without repetition.

    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    """
    def check(self, val: str, st: set[int]) -> bool:
        if val != ".":
            num: int = int(val)
            if num not in st:
                return False
            st.remove(num)

        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check row
        for i in range(9):
            st: set[int] = set(range(1, 10))
            for j in range(9):
                if not self.check(board[i][j], st):
                    return False
    
        # check cols
        for j in range(9):
            st: set[int] = set(range(1, 10))
            for i in range(9):
                if not self.check(board[i][j], st):
                    return False

        # check cells
        for k in range(9):
            row: int = k // 3
            col: int = k % 3

            st: set[int] = set(range(1, 10))

            for i in range(row * 3, row * 3 + 3):
                for j in range(col * 3, col * 3 + 3):
                    if not self.check(board[i][j], st):
                        return False

        return True
    
# def print_rows(board: list[list[str]]) -> None:
#     for i in range(9):
#         for j in range(9):
#             print(board[i][j], end=" ")
#         print("")            


# def print_cols(board: list[list[str]]) -> None:
#     for j in range(9):
#         for i in range(9):
#             print(board[i][j], end=" ")
#         print("")    

# def print3x3(board: list[list[str]]) -> None:
#         for k in range(9):
#             i = k//3
#             j = k%3
#             for row in range(i*3, i*3+3):
#                 for col in range(j*3, j*3+3):
#                     print(board[row][col], end=" ")
#                 print("")
#             print("-"*5)


def main() -> None:
    solution = Solution()
    
    b1 =[["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    # True
    print(f"Output: {solution.isValidSudoku(b1)}")

    b2 =[["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    #False
    print(f"Output: {solution.isValidSudoku(b2)}")

if __name__ == "__main__":
    main()