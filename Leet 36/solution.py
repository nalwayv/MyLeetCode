class Solution:
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        """
        Determines if a given 9x9 Sudoku board is valid.
        A Sudoku board is valid if:
        - Each row contains the digits 1-9 without repetition.
        - Each column contains the digits 1-9 without repetition.
        - Each of the nine 3x3 sub-boxes contains the digits 1-9 without repetition.
        - Empty cells are represented by the character '.'.
        Args:
            board (list[list[str]]): A 9x9 list of lists representing the Sudoku board.
        Returns:
            bool: True if the board is valid, False otherwise.
        """
        # rows
        for i in range(9):
            st: set[int] = set(range(1, 10))
            for j in range(9):
                if board[i][j] != '.':
                    num: int = int(board[i][j])
                    if num in st:
                        st.remove(num)
                    else:
                        return False
                    
        # cols
        for j in range(9):
            st: set[int] = set(range(1, 10))
            for i in range(9):
                if board[i][j] != '.':
                    num: int = int(board[i][j])
                    if num in st:
                        st.remove(num)
                    else:
                        return False
                    
        # boxes
        for k in range(9):
            r: int = k // 3
            c: int = k % 3    
            st: set[int] = set(range(1, 10))
            for i in range(r*3, r*3+3):
                for j in range(c*3, c*3+3):
                    if board[i][j] != '.':
                        num: int = int(board[i][j])
                        if num in st:
                            st.remove(num)
                        else:
                            return False
    
        return True


def main() -> None:
    print('36. Valid Sudoku')

    solution = Solution()
    
    case_1 = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9'],
    ]
    print(f'case 1 should equal True ? {solution.is_valid_sudoku(case_1) == True}')

    case_2 =[
        ['8','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9'],
    ]
    print(f'case 2 should equal False ? {solution.is_valid_sudoku(case_2) == False}')


if __name__ == '__main__':
    main()