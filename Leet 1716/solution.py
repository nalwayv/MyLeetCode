class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Compute the total amount of money saved in the "Leet Bank" after n days.
        
        Args:
            n (int):
                Number of days to simulate (non-negative). If n <= 0 return 0
        Returns:
            int:
                Total amount deposited after n days.
        """
        nums: list[int] = [1,2,3,4,5,6,7]
        total: int = 0
        for i in range(n):
            at: int = i % 7
            total += nums[at]
            nums[at] += 1
        return total


def test_case(sol: Solution, n: int, expected: int) -> None:
    result: int = sol.totalMoney(n)
    test: str = 'pass' if result == expected else 'fail'
    print(f'{n} should equal {expected}?: {test}')


def main() -> None:
    print('1716. Calculate Money in Leetcode Bank')
    
    solution = Solution()
    
    test_case(solution, 4, 10)
    test_case(solution, 10, 37)
    test_case(solution, 20, 96)


if __name__ == "__main__":
    main()