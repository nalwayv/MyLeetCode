class Solution:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table: dict[int, int] = {}

        for idx, num in enumerate(nums):
            if num not in table:
                table[target - num] = idx
            else:
                return [idx, table[num]]

        return nums


def main() -> None:
    solution = Solution()

    print("-"*5)

    nums1: list[int] = [2,7,11,15]
    target1: int = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")
    
    print("-"*5)

    nums2: list[int] = [3,2,45]
    target2: int = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")

    print("-"*5)


if __name__ == "__main__":
    main()