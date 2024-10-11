class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n: int = len(matrix)

        matrix2: list[list[int]] =  [[0 for _ in range(n)] for _ in range(n)]

        for c in range(n):
            for r in range(n):
                matrix2[c][n - r - 1] = matrix[r][c]

        for r in range(n):
            for c in range(n):
                matrix[r][c] = matrix2[r][c]


def print_matrix(matrix: list[list[int]]) -> None:
    n: int = len(matrix)
    for r in range(n):
        print("",end="")
        for c in range(n):
            print(f" {matrix[r][c]:02d} ", end="")
        print("")


def case1(sol: Solution) -> None:
    print("case1")
    matrix: list[list[int]] = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix)
    print_matrix(matrix)


def case2(sol: Solution) -> None:
    print("case2")
    matrix: list[list[int]] = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(matrix)
    print_matrix(matrix)


def main() -> None:
    print("48. Rotate Image")

    sol = Solution()

    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()