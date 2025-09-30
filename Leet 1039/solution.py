class Solution:
    def __init__(self):
        self.memo: dict[tuple[int, int], int] = {}

    def get_score(self, values: list[int], i: int, j: int) -> int:
        if i + 1 == j:
            return 0
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        score: float = float('inf')
        for k in range(i + 1, j):
            combination: int = values[i] * values[j] * values[k]
            new_score = combination + self.get_score(values, i, k) + self.get_score(values, k, j)
            score = min(score, new_score)
        
        self.memo[(i, j)] = int(score)

        return int(score)

    def minScoreTriangulation(self, values: list[int]) -> int:
        self.memo.clear()
        return self.get_score(values, 0, len(values) - 1)


def main() -> None:
    print('1039. Minimum Score Triangulation of Polygon')

    solution = Solution()

    print('Case 1')
    case1_values: list[int] = [1,2,3]
    case1_result: int = solution.minScoreTriangulation(case1_values)
    print(case1_result, 6)

    print('Case 2')
    case2_values: list[int] = [3,7,4,5]
    case2_result: int = solution.minScoreTriangulation(case2_values)
    print(case2_result, 144)

    print('Case 3')
    case3_values: list[int] = [1,3,1,4,1,5]
    case3_result: int = solution.minScoreTriangulation(case3_values)
    print(case3_result, 13)


if __name__ == '__main__':
    main()