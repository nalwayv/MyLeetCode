from typing import NamedTuple


class Keys(NamedTuple):
    value: int
    idx: int


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        #NOTE: sort matrix by column
        rows: int = len(score)
        cols: int = len(score[0])

        # sort
        sorted_k: list[Keys] = []
        for r in range(rows):
            sorted_k.append(Keys(score[r][k], r))
        sorted_k.sort(reverse=True)

        # rebuild
        result: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                result[r][c] = score[sorted_k[r].idx][c]

        return result


def main() -> None:
    print("2545. Sort the Students by Their Kth Score")

    score: list[list[int]] = [
        [10,6,9,1],
        [7,5,11,2],
        [4,8,3,15]]
    
    sol = Solution()
    result: list[list[int]] = sol.sortTheStudents(score, 2)
    
    print(result)


if __name__ == "__main__":
    main()