class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        Given a string s consisting of digits. Perform operations repeatedly until the string has exactly two digits
        and check if those two digits are equal.
        """
        nums: list[int] = [int(x) for x in s]
        
        p2: int = len(nums) - 1
        while p2 > 1:
            for i in range(p2):
                nums[i] = (nums[i] + nums[i+1]) % 10
            p2 -= 1

        return nums[0] == nums[1]


def test_case(sol: Solution, s: str, expected: bool) -> None:
    result: bool = sol.hasSameDigits(s)
    test: str = 'pass' if result == expected else 'fail'
    print(f'{s} should equal {expected}?: {test}')


def main() -> None:
    print('3461. Check If Digits Are Equal in String After Operations I')

    solution = Solution()

    test_case(solution, '3902', True)
    test_case(solution, '34789', False)


if __name__ == '__main__':
    main()