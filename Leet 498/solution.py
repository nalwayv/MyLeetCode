from typing import Callable


class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        Returns the elements of the given 2D matrix in diagonal order.

        The traversal starts from the top-left element and alternates between moving
        up-right and down-left along the diagonals of the matrix. When the traversal
        reaches the boundary of the matrix, it changes direction and continues until
        all elements have been visited.

        Args:
            mat (list[list[int]]): A 2D list representing the matrix.

        Returns:
            list[int]: A list of integers representing the matrix elements in diagonal order.

        Example:
            Input: mat = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
        """
        rows: int = len(mat)
        cols: int = len(mat[0])

        on_grid: Callable[[int, int], bool] = lambda x, y: x >= 0 and x < rows and y >= 0 and y < cols

        result: list[int] = []
        move_up: bool  = True
        r: int = 0
        c: int = 0
        for _ in range(rows * cols):
            result.append(mat[r][c])

            if move_up:
                # diaginal
                if on_grid(r-1, c+1):
                    r -= 1
                    c += 1
                else:
                    # across
                    # down
                    move_up = False
                    if on_grid(r, c+1):
                        c += 1
                    elif on_grid(r+1, c):
                        r += 1
            else:
                # diagonal
                if on_grid(r+1, c-1):
                    r += 1
                    c -= 1
                else:
                    # down
                    # across
                    move_up = True
                    if on_grid(r+1, c):
                        r += 1
                    elif on_grid(r, c+1):
                        c += 1

        return result


def case_1(sol: Solution) -> None:
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    result: list[int] = sol.findDiagonalOrder(mat)
    print(f"case 1 {result}")


def case_2(sol: Solution) -> None:
    mat = [[1,2],
           [3,4]]
    result: list[int] = sol.findDiagonalOrder(mat)
    print(f"case 2 {result}")


def case_3(sol: Solution) -> None:
    mat = [
        [1,2,3,4],
        [5,6,7,8]]
    result: list[int] = sol.findDiagonalOrder(mat)
    print(f"case 3 {result}")


def main() -> None:
    print("498. Diagonal Traverse")
    sol = Solution()
    case_1(sol)
    case_2(sol)
    case_3(sol)


if __name__ == "__main__":
    main()