from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        """Finds the smallest non-negative integer that cannot be formed.

        Args:
            nums (list[int]): A list of integers.
            value (int): The value to add or subtract.

        Returns:
            int: The smallest non-negative integer that cannot be formed.
        """
        frequency: Counter[int] = Counter(num % value for num in nums)

        mex: int = 0

        while frequency[mex % value] > 0:
            frequency[mex % value] -= 1
            mex += 1

        return mex


def main() -> None:
    print('2598. Smallest Missing Non-negative Integer After Operations')
    sol = Solution()

    case1: int = sol.findSmallestInteger(nums= [1,-10,7,13,6,8], value= 5)
    print(case1)

    case2: int = sol.findSmallestInteger(nums= [1,-10,7,13,6,8], value= 7)
    print(case2)


if __name__ == '__main__':
    main()