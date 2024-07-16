class Solution:
    """
    Given an integer array nums of 2n integers,

    group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)

    such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
    """
    def arrayPairSum(self, nums: list[int]) -> int:
        n: int = len(nums)
        sorted_nums: list[int] = sorted(nums)

        result: int = 0
        for i in range(1, n, 2):
            result += min(sorted_nums[i-1], sorted_nums[i])

        return result


def main() -> None:
    solution = Solution()
    nums1: list[int] = [1,4,3,2]
    print(f"Output: {solution.arrayPairSum(nums1)}")
    nums2: list[int] = [6,2,6,5,1,2]
    print(f"Output: {solution.arrayPairSum(nums2)}")


if __name__ == "__main__":
    main()