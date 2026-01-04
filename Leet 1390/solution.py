class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        total: int = 0

        for num in nums:
            values: list[int] = []
            sq: int = int(num ** 0.5)
            for i in range(1, sq + 1):
                if num % i == 0:
                    if i*i != num:
                        values.extend([i, num // i])
                    else:
                        values.append(i)

            if len(values) == 4:
                total += sum(values)

        return total


def test_cast(sol: Solution, nums: list[int], expected: int):
    test_result: str = 'pass' if sol.sumFourDivisors(nums) == expected else 'fail'
    print(f'Test case for {nums} should equal {expected}: {test_result}')


def main() -> None:
    print('1390. Four Divisors')

    solution = Solution()
    test_cast(solution, [21,4,7], 32)


if __name__ == '__main__':
    main()