class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        rows: int = len(mat)
        cols: int = len(mat)
        if rows != cols:
            return -1

        result: int = 0
        start: int = 0
        end: int = cols - 1
        for i in range(rows):
            if start == end:
                result += mat[i][start]
            else:
                result += mat[i][start] + mat[i][end]
            start += 1
            end -= 1

        return result


def main() -> None:
    print("1572. Matrix Diagonal Sum")

    sol = Solution()
    mat1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    print(f"Case 1 should equal 25: {sol.diagonalSum(mat1)}")
    
    mat2 = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
    print(f"Case 1 should equal 8: {sol.diagonalSum(mat2)}")


if __name__ == "__main__":
    main()
        