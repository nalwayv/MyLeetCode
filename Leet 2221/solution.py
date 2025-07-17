class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        """
        Calculates the triangular sum of an array of integers.
        The triangular sum is obtained by repeatedly replacing the array with a new array where each element is the sum of adjacent elements modulo 10, until only one element remains. The function returns the final sum of all elements left in the stacks after the process.
        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The sum of the remaining elements after performing the triangular sum process.
        Example:
            >>> triangularSum([1,2,3,4,5])
            8
        """
        while len(nums) > 1:
            for i in range(len(nums)-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            nums.pop()
        return nums[0]


def main() -> None:
    print("2221. Find Triangular Sum of an Array")

    sol = Solution()

    print(sol.triangularSum(nums=[1,2,3,4,5]), "== 8")
    print(sol.triangularSum(nums=[5]), "== 5")
    print(sol.triangularSum(nums=[1,2]), "== 3")


if __name__ == "__main__":
    main()
        