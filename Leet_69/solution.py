class Solution:
    def mySqrt(self, x: int) -> int:
        n1: int = x
        n2: int = 1

        while (n1 - n2) > 0:
            n1 = (n1 + n2) // 2
            n2 = x // n1
        
        return n1


def main() -> None:
    solution = Solution()
    print(f"MySqrt(4) == 2 ? {solution.mySqrt(4) == 2}")
    print(f"MySqrt(8) == 2 ? {solution.mySqrt(8) == 2}")
    print(f"MySqrt(25) == 5 ? {solution.mySqrt(8) == 2}")

if __name__ == "__main__":
    main()