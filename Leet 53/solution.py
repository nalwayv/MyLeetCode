class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Given an integer array nums, find the subarray with the largest sum, and return its sum.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The subarray with the lergest sum.
        """
        c: int = nums[0]
        m: int = nums[0]
        for i in range(1, len(nums)):
            c = max(nums[i], c + nums[i])
            m = max(m, c)
        return m


def main() -> None:
    print('53. Maximum Subarray')
    sol = Solution()
    case1: int = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(f'Case 1 should equal 6? {'pass' if case1 == 6 else 'fail'}')


if __name__ == '__main__':
    main()