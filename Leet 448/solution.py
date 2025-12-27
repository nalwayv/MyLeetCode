class Solution:
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        snums = set(nums)
        result: list[int] = []
        for i in range(len(nums)):
            if i+1 not in snums:
                result.append(i+1)
        return result


def main() -> None:
    print('448. Find All Numbers Disappeared in an Array')
    solution = Solution()
    nums: list[int] = [4,3,2,7,8,2,3,1]
    case1: list[int] = solution.find_disappeared_numbers(nums)
    print(case1)


if __name__ == '__main__':
    main()