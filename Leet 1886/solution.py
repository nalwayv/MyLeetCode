class Solution:
    # def check_for_match(self, mat: list[list[int]], target: list[list[int]]) -> bool:
    #     mat_rows: int = len(mat)
    #     mat_cols: int = len(mat[0])
    #     if mat_rows != len(target) or mat_cols != len(target[0]):
    #         return False
        
    #     for i in range(mat_rows):
    #         for j in  range(mat_cols):
    #             if mat[i][j] != target[i][j]:
    #                 return False
    #     return True

    def rotate_matrix(self, mat: list[list[int]]) -> list[list[int]]:
        mat_rows: int = len(mat)
        mat_cols: int = len(mat[0])

        rotated: list[list[int]] = [[0 for _ in range(mat_rows)] for _ in range(mat_cols)]

        for i in range(mat_cols):
            for j in range(mat_rows):
                rotated[i][j] = mat[mat_rows - j - 1][i]

        return rotated
    
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            mat = self.rotate_matrix(mat)
            if mat == target:
                return True
        return False


def test_case(sol: Solution, mat: list[list[int]], target: list[list[int]], expected: bool):
    test_case = sol.findRotation(mat, target)
    result = 'pass' if test_case == expected else 'fail'
    print(f'findRotation for mat and target should equal {expected}? {result}')


def main() -> None:
    print('1886. Determine Whether Matrix Can Be Obtained By Rotation')
    sol = Solution()

    test_case(sol, [[0,1],[1,0]], [[1,0],[0,1]], True)
    test_case(sol, [[0,1],[1,1]], [[1,0],[0,1]], False)
    test_case(sol, [[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]], True)
    test_case(sol, [[0,0], [0, 1]], [[0,0], [1,0]], True)


if __name__ == '__main__':
    main()