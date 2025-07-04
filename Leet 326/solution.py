class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1


def main() -> None:
    print("326. Power of Three")
    sol = Solution()
    print(sol.isPowerOfThree(27))
    print(sol.isPowerOfThree(0))
    print(sol.isPowerOfThree(-2 ** 31))
    print(sol.isPowerOfThree(2 ** 31))


if __name__ == "__main__":
    main()