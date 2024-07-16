class Solution:
    """
    Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

    Example 1:

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]

    Example 2:

    Input: nums = [1,1]
    Output: [2]


    Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n
    """

    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        # build table n+1 
        # will be excluding 0
        n: int = len(nums)
        table: list[bool] = [True] * (n+1)

        # update table with used numbers
        for num in nums:
            table[num] = False

        # collect unused numbers and return
        result: list[int] = []
        for i in range(1, n+1):
            if table[i]:
                result.append(i)

        return result
        

def main() -> None:
    solution = Solution()
    nums: list[int] = [4,3,2,7,8,2,3,1]
    result: list[int] = solution.find_disappeared_numbers(nums)

    print(f"Input: {nums}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()