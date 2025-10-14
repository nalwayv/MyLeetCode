class Solution:
    def is_increasing(self, nums: list[int], start: int, k: int):
        for i in range(start, start + k - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True

    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n: int = len(nums)
        for i in range(n - 2 * k + 1) :
            if self.is_increasing(nums, i, k) and self.is_increasing(nums, i + k, k):
                return True
        return False
    

def main() -> None:
    print('3349. Adjacent Increasing Subarrays Detection I')

    sol = Solution()

    print(sol.hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3))
    print(sol.hasIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7], k = 5))
    print(sol.hasIncreasingSubarrays(nums = [0,4,16,20,-6], k = 2))
    print(sol.hasIncreasingSubarrays(nums = [5,8,-2,-1], k = 2))


if __name__ == '__main__':
    main()
