class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        result: float = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                result = min(result, abs(i - start))
        return int(result)


def main() -> None:
    print('1848. Minimum Distance to the Target Element')
    
    sol = Solution()
    result = sol.getMinDistance(nums=[1,2,3,4,5],target=5, start=3)
    print(f'Min Dist To Target: {result}')


if __name__ == '__main__':
    main()