class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        binary_number: int = 0
        result: list[bool] = [False] * len(nums)

        for i, num in enumerate(nums):
            binary_number = (binary_number << 1) | num
            if binary_number % 5 == 0:
                result[i] = True

        return result


def main() -> None:
    print('1018. Binary Prefix Divisible By 5')
    solution = Solution()
    case1: list[bool] = solution.prefixesDivBy5([0,1,1])
    print(case1)


if __name__ == '__main__':
    main()