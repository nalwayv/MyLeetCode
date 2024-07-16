class Solution:
    """
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

    Example:

    Input: nums = [1,7,3,6,5,6]
    
    Output: 3
    
    Explanation:

    The pivot index is 3.

    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11

    Right sum = nums[4] + nums[5] = 5 + 6 = 11
    """
    def pivotIndex(self, nums: list[int]) -> int:
        # start with right as total sum
        # then as pivot moves up
        # subtract current [i] from right
        # check if left and right equil else add current [i] to left

        n: int = len(nums)
        right: int = sum(nums)
        left: int = 0

        for i in range(n):
            # treat current nums[i] as pivot
            # and check if total between left and right
            right -= nums[i]

            if right == left:
                return i
            
            left += nums[i]

        return -1


def main() -> None:
    solution = Solution()
    case1: list[int] = [1,7,3,6,5,6]
    case2: list[int] = [1,2,3]
    case3: list[int] = [2,1,-1]

    print(f"case1 {solution.pivotIndex(case1)}")
    print(f"case2 {solution.pivotIndex(case2)}")
    print(f"case3 {solution.pivotIndex(case3)}")


if __name__ == "__main__":
    main()