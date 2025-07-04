class Solution:
    """
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    
    Example 1:
        Input: rowIndex = 3
        Output: [1,3,3,1]
    """
    def getRow(self, rowIndex: int) -> list[int]:
        result: list[int] = [0] * (rowIndex + 1)
        i: int = rowIndex + 1
        num: int = 1
        for j in range(1, i+1):
            result[j-1] = num
            num = num * (i-j) // j
        return result


    def getRowRecursive(self, rowIndex: int) -> list[int]:
        def recursive(i: int, j: int, num: int, result: list[int]) -> None:
            if j >= (i + 1):
                return
            result[j-1] = num
            num = num * (i-j) // j
            recursive(i, j+1, num, result)

        result: list[int] = [0] * (rowIndex + 1)
        recursive(rowIndex+1, 1, 1, result)
        return result


def main() -> None:
    solution = Solution()
    print(f"Output: {solution.getRow(0)}")
    print(f"Output: {solution.getRow(1)}")
    print(f"Output: {solution.getRow(3)}")

    print(f"Output R: {solution.getRowRecursive(0)}")
    print(f"Output R: {solution.getRowRecursive(1)}")
    print(f"Output R: {solution.getRowRecursive(3)}")


if __name__ == "__main__":
    main()