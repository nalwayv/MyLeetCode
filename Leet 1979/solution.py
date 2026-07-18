import math
from typing import List


def find_gcd(nums: List[int]) -> int:
    """Return the Greatest Common Devisor of the smallest and largest number from nums.

    Args:
        nums (List[int]): list of ints.
    
    Returns:
        int: GCD of the smallest and largest number from nums.
    """
    mx: int = nums[0]
    mn: int = nums[0]
    
    for num in nums:
        mx = max(mx, num)
        mn = min(mn, num)

    return math.gcd(mn, mx)


def main() -> None:
    print("1979. Find Greatest Common Divisor of Array")
    
    nums: List[int] = [2, 5, 6, 9, 10]
    result: str = "pass" if find_gcd(nums) == 2 else "fail"
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
