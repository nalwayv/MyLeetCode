class Solution:
    def is_palindromic(self, arr: list[int]) -> bool:
        """
        Check is arr is a palindrome

        Args:
            arr (list[int])

        Returns:
            True if arr is palindromic
        """
        p1: int = 0
        p2: int = len(arr) - 1
        while p1 < p2:
            if arr[p1] != arr[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

    def to_base(self, n: int, base: int) -> list[int]:
            """
            Convert n to a list repersentation of its base form
            
            Args:
                n (int):
                base (int):

            Returns:
                list[int]:
            """
            arr: list[int] = []
            if n <= 1:
                return arr
            
            while n > 0:
                r: int = n % base
                arr.insert(0, r)
                n //= base
            return arr

    def isStrictlyPalindromic(self, n: int) -> bool:
        """
        An integer n is strictly palindromic if, 
        - for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.
        
        So 9 to base 2 = 1001 which is palindeomic but 9 to base 3 = 100 making 9 not a strictly palindromic number.
        
        Args: 
            n (int): check is every base until n is palindromic
        
        Returns:
            bool: if n is a strictly palindromic number
        """
        for i in range(2, n-1):
            if not self.is_palindromic(self.to_base(n, i)):
                return False
        return True


# TEST CASE ___


def test_case(sol: Solution, n: int, expected: bool) -> None:
    result: str = "pass" if sol.isStrictlyPalindromic(n) == expected else "fail"
    print(f"Test Case {n}: {result}")


# MAIN ___


def main() -> None:
    print("2396. Strictly Palindromic Number")

    sol = Solution()

    test_case(sol, 9, False)
    test_case(sol, 4, False)


if __name__ == "__main__":
    main()