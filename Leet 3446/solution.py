class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Sorts the diagonals of a square matrix in-place.
        For each diagonal above the main diagonal (upper diagonals), sorts the elements in ascending order.
        For each diagonal below and including the main diagonal (lower diagonals), sorts the elements in descending order.
        Args:
            grid (list[list[int]]): A square matrix represented as a list of lists of integers.
        Returns:
            list[list[int]]: The matrix after sorting its diagonals as specified.
        """
        rows: int = len(grid)

        # upper
        for j in range(1, rows):
            tmp: list[int] = [grid[i][j + i] for i in range(rows - j)]
            print(tmp)
            tmp.sort()
            for i in range(rows - j):
                grid[i][j+i] = tmp[i]

        # lower
        for i in range(rows):
            tmp: list[int] = [grid[i + j][j] for j in range(rows - i)]
            tmp.sort(reverse=True)
            for j in range(rows-i):
                grid[i+j][j] = tmp[j]

        return grid


def print_grid(grid: list[list[int]]) -> None:
    r = len(grid)
    c = len(grid[0])

    for x in range(r):
        print("[",end="")
        for y in range(c):
            print(f" {grid[x][y]} ", end="")
        print("]")


def case1(sol: Solution) -> None:
    print("case 1")
    grid = [
        [1,7,3],
        [9,8,2],
        [4,5,6]]
    
    # [8 2 3]
    # [9 6 7]
    # [4 5 1]
    print_grid(sol.sortMatrix(grid))


def case2(sol: Solution) -> None:
    print("case 2")
    grid = [
        [0,1],
        [1,2]]
    
    # [2 1]
    # [1 0]
    print_grid(sol.sortMatrix(grid))


def case3(sol: Solution) -> None:
    print("case 3")
    grid = [
        [-1,-2,-3],
        [-3,-3,-2],
        [-4,-4,0]]
    
    # [  0 -2 -3 ]
    # [ -3 -1 -2 ]
    # [ -4 -4 -3 ]
    print_grid(sol.sortMatrix(grid))


def main() -> None:
    print("3446. Sort Matrix by Diagonals")

    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()