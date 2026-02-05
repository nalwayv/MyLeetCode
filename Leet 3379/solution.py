class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        def wrapi(value: int, lo: int, hi: int) -> int:
            return lo + ((value - lo) % (hi - lo) + (hi - lo)) % (hi - lo);

        n: int = len(nums)
        result: list[int] = [0] * n
        for i, num in enumerate(nums):
            result[i] = nums[wrapi(i + num, 0, n)]
        return result
    

def main() -> None:
    print('3379. Transformed Array')
    solution = Solution()
    test_cases = [
        [3, -2, 1, 1],
        [-1, 4, -1]
    ]
    for nums in test_cases:
        print(solution.constructTransformedArray(nums))


if __name__ == '__main__':
    main()