import math
from typing import List


def gcd_sum(nums: List[int]) -> int:
    """Return the sum of all pairs from a non-decreasing prefix gcd.

    Args:
        nums: (List[int]): list of ints of length n

    Returns:
        int: sum of all pairs from prefix gcd were smallest is paired with the largest.
    """
    n: int = len(nums)

    prefix_gcd: List[int] = [0] * n
    mx: int = nums[0]
    for i in range(n):
        mx = max(mx, nums[i])
        prefix_gcd[i] = math.gcd(nums[i], mx)

    sorted_prefix_gcd: List[int] = sorted(prefix_gcd)

    lo: int = 0
    hi: int = n - 1
    result: int = 0
    while lo < hi:
        result += math.gcd(sorted_prefix_gcd[lo], sorted_prefix_gcd[hi])
        lo += 1
        hi -= 1

    return result


def test_case(nums: List[int], expected: int) -> None:
    result: int = gcd_sum(nums)
    test_result: str = "pass" if result == expected else "fail"
    print(f"Result: {test_result}")


def main() -> None:
    print("3867. Sum of GCD of Formed Pairs")

    nums1: List[int] = [2, 6, 4]
    test_case(nums1, 2)

    nums2: List[int] = [3, 6, 2, 8]
    test_case(nums2, 5)


if __name__ == "__main__":
    main()
