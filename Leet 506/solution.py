class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sort_score: list[int] = sorted(score, reverse=True)
        table: dict[int, str] = {num: str(i + 1) for i,num in enumerate(sort_score)}

        n: int = len(score)
        medals: list[str] = ["Gold Medal", "Silver Medal","Bronze Medal"]
        for i in range(3):
            if i < n:
                table[sort_score[i]] = medals[i]

        return [table[num] for num in score]