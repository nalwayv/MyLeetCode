class Solution:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.
    """
    def singleNumber(self, nums: list[int]) -> int:
        hash_set: set[int] = set()
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                hash_set.remove(num)

        return hash_set.pop() if hash_set else -1


def main() -> None:
    solution = Solution()

    nums1: list[int] = [2,2,1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.singleNumber(nums1)}")

    nums2: list[int] = [4,1,2,1,2]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.singleNumber(nums2)}")

    nums3: list[int] = [1]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.singleNumber(nums3)}")


if __name__ == "__main__":
    main()
        