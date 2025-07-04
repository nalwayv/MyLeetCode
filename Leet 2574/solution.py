class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """
        Calculates the left and right sum differences of nums

        Args:
            nums (list[int]): A list of integers.

        Returns:
            list[int]: sum difference between left and right.
        """
        n: int = len(nums)
        left: int = 0
        right: int = sum(nums[1:])
        result: list[int] = []

        for i in range(n):
            result.append(abs(left - right))
            left += nums[i]
            if i + 1 < n:
                right -= nums[i + 1]
        
        return result


def main() -> None:
    print("2574. Left and Right Sum Differences")

    sol = Solution()
    
    print(sol.leftRightDifference([10,4,8,3]))
    print(sol.leftRightDifference([1,2,3,3,2,1]))
    print(sol.leftRightDifference([1]))


if __name__ == "__main__":
    main()
        