class Solution:
    """
    https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
   
    Third Maximum Number

    Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

    Example 1:

    Input: nums = [3,2,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2.
    The third distinct maximum is 1.
    

    Example 2:

    Input: nums = [2,2,3,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2 (both 2's are counted together since they have the same value).
    The third distinct maximum is 1.


    Constraints:

    1 <= nums.length <= 10**4
    -2**31 <= nums[i] <= 2**31 - 1
    """

    def third_max(self, nums: list[int]) -> int:
        """working on
        """
        n: int = len(nums)
        if n <= 1:
            return nums[0]
        
        if n <= 2:
            return max(nums[0], nums[1])

        sort: list[int] = sorted(nums)
        maxs: list[int] = [sort[-1], 0, 0]
        k: int = 1

        for i in reversed(range(n-1)):
            current: int = sort[i]

            if current != maxs[k-1]:
                maxs[k] = current
                k+=1

            if k == 3:
                return maxs[-1]            

        return max(maxs)


def main() -> None:
    solution = Solution()
    nums: list[int] = [2,2,3,1]
    result: int = solution.third_max(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")

if __name__ == "__main__":
    main()
        