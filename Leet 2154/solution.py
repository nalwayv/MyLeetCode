class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while original in set(nums):
            original *= 2
        return original