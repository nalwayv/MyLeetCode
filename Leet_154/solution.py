class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo: int = 0
        hi: int = len(nums) - 1

        while lo < hi:
            mid: int = (lo+hi) // 2
            target: int = nums[hi]

            if target == nums[mid]:
                hi -= 1
            elif nums[mid] < target:
                hi = mid
            else:
                lo = mid + 1

        return nums[lo]