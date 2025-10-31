class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        table: dict[int, int] = {}
        result: list[int] = []
        
        for num in nums:
            table[num] = table.get(num, 0) + 1
            if table[num] > 1:
                result.append(num)

            if len(result) == 2:
                break
        return result


def test_case(solution: Solution, nums: list[int], expected: list[int]):
    result: list[int] = solution.getSneakyNumbers(nums)
    result.sort()

    test_result: str = 'pass' if result == expected else 'fail'
    print(f'{nums} should equal {expected}? {test_result}')


def main() -> None:
    print('3289. The Two Sneaky Numbers of Digitville')

    solution = Solution()

    test_case(solution, [0,1,1,0], [0,1])
    test_case(solution, [0,3,2,1,3,2], [2,3])
    test_case(solution, [7,1,5,4,3,4,6,0,9,5,8,2], [4,5])


if __name__ == '__main__':
    main()