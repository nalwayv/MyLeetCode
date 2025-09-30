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
        length: int = len(nums)

        while length > 1:
            for i in range(length - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            length -= 1
            
        return nums[0]


def main() -> None:
    print('2221. Find Triangular Sum of an Array')

    sol = Solution()

    print(f'case 1 should equal 8 ? {sol.triangularSum(nums=[1,2,3,4,5])}')
    print(f'case 2 should equal 5 ? {sol.triangularSum(nums=[5])}')
    print(f'case 3 should equal 3 ? {sol.triangularSum(nums=[1,2])}')


if __name__ == '__main__':
    main()
        