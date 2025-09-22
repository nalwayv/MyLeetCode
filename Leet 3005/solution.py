class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """
        Calculates the total number of elements in the input list `nums` that have the maximum frequency.
        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The sum of frequencies of all elements that appear with the maximum frequency.
        """
        frequency: dict[int, int] = {}
        max_frequency: int = -1
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            max_frequency = max(max_frequency, frequency[num])

        return sum([v for v in frequency.values() if v == max_frequency])


def main() -> None:
    print('3005. Count Elements With Maximum Frequency')
    
    solution = Solution()

    print(f'case 1 should equal 4? {solution.maxFrequencyElements(nums= [1,2,2,3,1,4])}')
    print(f'case 2 should equal 5? {solution.maxFrequencyElements(nums= [1,2,3,4,5])}')
    print(f'case 3 should equal 4? {solution.maxFrequencyElements(nums= [1,1,2,2])}')


if __name__ == '__main__':
    main()