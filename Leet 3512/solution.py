class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        if total % k == 0:
            return 0

        count: int = 0
        while total % k != 0:
            count += 1
            total -= 1

        return count


def main() -> None:
    print('3512. Minimum Operations to Make Array Sum Divisible by K')

    solution = Solution()

    print(solution.minOperations([3, 9, 7], 5))
    print(solution.minOperations([4, 1, 3], 4))
    print(solution.minOperations([3, 2], 6))


if __name__ == '__main__':
    main()