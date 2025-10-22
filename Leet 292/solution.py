class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 > 0
    

def test_case(solution: Solution, n: int, expected: bool) -> None:
    result = solution.canWinNim(n)
    expected_str = 'True,' if expected else 'False,'
    print(f'{n} should equal {expected_str.ljust(7)} result: {result}')


def main() -> None:
    print('292. Nim Game')
    sol = Solution()
    test_case(sol, 4, False)
    test_case(sol, 1, True)
    test_case(sol, 2, True)


if __name__ == '__main__':
    main()