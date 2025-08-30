class Solution:
    def is_power_of_four(self, n: int) -> bool:
        """
        Determines whether a given integer is a power of four.
        Args:
            n (int): The integer to check.
        Returns:
            bool: True if n is a power of four, False otherwise.
        """
        if n == 0:
            return False

        while n % 4 == 0:
            n //= 4
    
        return n == 1


def main() -> None:
    print('342. Power of Four')

    solution = Solution()
    
    print(f'case 1 should equal true ? {solution.is_power_of_four(n=16) == True}')
    print(f'case 2 should equal false ? {solution.is_power_of_four(n=5) == False}')
    print(f'case 3 should equal true ? {solution.is_power_of_four(n=1) == True}')


if __name__ == '__main__':
    main()