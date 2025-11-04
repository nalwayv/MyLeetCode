from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n:int = len(nums)
        result: list[int] = []

        for i in range(n - k + 1):
            counter = Counter(nums[i : i + k])
            freq: list[tuple[int, int]] = sorted(counter.items(), key=lambda item: (-item[1], -item[0]))
            x_sum: int = sum(key * value for key, value in freq[:x])

            result.append(x_sum)

        return result


def main() -> None:
    print('3318. Find X-Sum of All K-Long Subarrays I')
    
    solution = Solution()
    print(solution.findXSum([1,1,2,2,3,4,2,3], 6, 2))


if __name__ == '__main__':
    main()
        