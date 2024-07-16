class Solution:
    """Given an m x n matrix, return all elements of the matrix in spiral order.
    
    Example1:
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]

    Example2:
        Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """

    def in_range(self, i: int, j: int, x: int, y: int):
        return (i >= 0 and i < x) and (j >= 0 and j < y)
    
    def create_matrix(self, m: int, n:int) -> list[list[bool]]:
        mat: list[list[bool]] = []
        for _ in range(m):
            mat.append([False for _ in range(n)])
        return mat
    
    def is_full(self, matrix: list[list[bool]], m: int, n: int):
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == False:
                    return False
        return True

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m: int = len(matrix)
        n: int = len(matrix[0])

        checked: list[list[bool]] = self.create_matrix(m,n)
        checked[0][0] = True

        result: list[int] = [matrix[0][0]]

        LEFT: int = 0
        RIGHT: int = 1
        UP: int = 2
        DOWN: int = 3

        i: int = 0
        j: int = 0
        direction: int = LEFT

        while True:
            if direction == LEFT:
                if self.in_range(i, j+1, m, n) and not checked[i][j+1]:
                    j += 1
                    checked[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = DOWN

            if direction == DOWN:
                if self.in_range(i+1, j, m, n) and not checked[i+1][j]:
                    i += 1
                    checked[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = RIGHT
            
            if direction == RIGHT:
                if self.in_range(i, j-1, m, n) and not checked[i][j-1]:
                    j -= 1
                    checked[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = UP

            if direction == UP:
                if self.in_range(i-1, j, m, n) and not checked[i-1][j]:
                    i -= 1
                    checked[i][j] = True
                    result.append(matrix[i][j])
                else:
                    direction = LEFT

            if self.is_full(checked, m, n):
                break
   
        return result


def main() -> None:
    solution = Solution()
    matrix: list[list[int]] = [
        [1,2,3,4,5,6,7,8,9,10],
        [11,12,13,14,15,16,17,18,19,20],
        [21,22,23,24,25,26,27,28,29,30],
        [31,32,33,34,35,36,37,38,39,40],
        [41,42,43,44,45,46,47,48,49,50],
        [51,52,53,54,55,56,57,58,59,60],
        [61,62,63,64,65,66,67,68,69,70],
        [71,72,73,74,75,76,77,78,79,80],
        [81,82,83,84,85,86,87,88,89,90],
        [91,92,93,94,95,96,97,98,99,100]
    ]    
    result: list[int] = solution.spiralOrder(matrix)
    print(result)


if __name__ == "__main__":
    main()