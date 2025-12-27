class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count: int = 0
        count: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                max_count = max(max_count, count)
        return max_count


def main() -> None:
    print('485. Max Consecutive Ones')
    sol = Solution()
    case1 = sol.findMaxConsecutiveOnes([1,1,0,1,1,1])
    print(case1)


if __name__ == '__main__':
    main()