class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows: int = len(mat)
        cols: int = len(mat[0])

        if (rows == r and cols == c) or (rows*cols != r*c):
            return mat

        result: list[list[int]] = [[0 for _ in range(c)] for _ in range(r)]

        i: int = 0
        j: int = 0
        
        for x in range(rows):
            for y in range(cols):
                result[i][j] = mat[x][y]
                j += 1
                if j >= c:
                    j = 0
                    i += 1

        return result


# __ Test Cases


def case_1(sol: Solution) -> None:
    print("Case 1: 2x2 => 1x4")

    mat: list[list[int]] = [
        [1,2],
        [3,4]
    ]
    rows: int = 1
    cols: int = 4

    result: list[list[int]] = sol.matrixReshape(mat, rows, cols)
    for r in range(len(result)):
        print("[",end="")
        for c in range(len(result[0])):
            print(f" {result[r][c]} ", end="")
        print("]")


def case_2(sol: Solution) -> None:
    print("Case 2: => return same")

    mat: list[list[int]] = [
        [1,2],
        [3,4]
    ]
    rows: int = 2
    cols: int = 4

    result: list[list[int]] = sol.matrixReshape(mat, rows, cols)
    for r in range(len(result)):
        print("[",end="")
        for c in range(len(result[0])):
            print(f" {result[r][c]} ", end="")
        print("]")


def case_3(sol: Solution) -> None:
    print("Case 3: 4x2 => 2*4")

    mat: list[list[int]] = [
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ]
    rows: int = 2
    cols: int = 4

    result: list[list[int]] = sol.matrixReshape(mat, rows, cols)
    for r in range(len(result)):
        print("[",end="")
        for c in range(len(result[0])):
            print(f" {result[r][c]} ", end="")
        print("]")


def case_4(sol: Solution) -> None:
    print("Case 4: 1x2 => 2x1")

    mat: list[list[int]] = [[1,2]]
    rows: int = 2
    cols: int = 1

    result: list[list[int]] = sol.matrixReshape(mat, rows, cols)
    for r in range(len(result)):
        print("[",end="")
        for c in range(len(result[0])):
            print(f" {result[r][c]} ", end="")
        print("]")


# __ Main


def main() -> None:
    print("566. Reshape the Matrix")

    sol = Solution()
    
    case_1(sol)
    case_2(sol)
    case_3(sol)
    case_4(sol)


if __name__ == "__main__":
    main()