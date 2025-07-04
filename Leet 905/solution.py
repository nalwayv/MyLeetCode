class Solution:
    """
    Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

    Return any array that satisfies this condition.

    Example 1:

    Input: nums = [3,1,2,4]
    Output: [2,4,3,1]
    Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

    Example 2:

    Input: nums = [0]
    Output: [0]


    Constraints:

        1 <= nums.length <= 5000
        0 <= nums[i] <= 5000
    """
    def is_even(self, num: int) -> bool:
        return (num & 1) == 0

    def is_odd(self, num: int) -> bool:
        return (num & 1) != 0

    def sort_array_by_parity(self, nums: list[int]) -> list[int]:
        """
        sort with evens to the left and odds to the right
        """
        n: int = len(nums)
        if n <= 1:
            return nums

        lo: int = 0
        hi: int = n-1

        while lo < hi:
            if self.is_odd(nums[lo]) and self.is_even(nums[hi]):
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo+=1
                hi-=1
            elif self.is_even(nums[lo]) and self.is_odd(nums[hi]):
                lo+=1
                hi-=1
            elif self.is_even(nums[lo]) and self.is_even(nums[hi]):
                lo+=1
            else:
                hi-=1

        return nums


def main() -> None:
    solution = Solution()
    nums: list[int] = [3,1,2,4]
    print(f"Input: {nums}")
    nums = solution.sort_array_by_parity(nums)
    print(f"Output: {nums}")


if __name__ == "__main__":
    main()