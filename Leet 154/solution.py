class Solution:
    def findMin(self, nums: list[int]) -> int:
        result: int = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] < 0:
                result = min(result, nums[i + 1])
        return result;