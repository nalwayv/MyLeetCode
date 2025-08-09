class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines if a given integer is a power of two.
        Args:
            n (int): The integer to check.
        Returns:
            bool: True if n is a power of two, False otherwise.
        """
        if n == 0:
            return False
        
        while n % 2 == 0:
            n //= 2

        return n == 1


def main() -> None:
    print("231. Power of Two")

    sol = Solution()
    
    print(f"1 should be a power of 2 ? {sol.isPowerOfTwo(1)}")
    print(f"16 should be a power of two ? {sol.isPowerOfTwo(16)}")
    print(f"13 should not be a power of two ? {not sol.isPowerOfTwo(13)}")
    print(f"8 should be a power of two ? {sol.isPowerOfTwo(8)}")


if __name__ == "__main__":
    main()
