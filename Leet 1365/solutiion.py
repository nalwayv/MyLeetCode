class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result: list[int] = [0] * len(nums)
        snums: list[int] = sorted(nums)
        for i, num in enumerate(nums):
            result[i] = snums.index(num)
        return result


def main() -> None:
    print('1365. How Many Numbers Are Smaller Than the Current Number')
    sol = Solution()
    case1: list[int] = sol.smallerNumbersThanCurrent([8,1,2,2,3])
    print(case1)


if __name__ == '__main__':
    main()