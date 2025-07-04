class Solution:
    def mySqrt(self, x: int) -> int:
        n1: int = x
        n2: int = 1

        while (n1 - n2) > 0:
            n1 = (n1 + n2) // 2
            n2 = x // n1
        
        return n1
    
    def mySqrtBS(self, x: int) -> int:
        """Using BinarySearch
        """
        if x == 1:
            return 1
        
        lo: int = 1
        hi: int = x//2
        result: int = 0

        while lo <= hi:
            mi: int = (lo + hi) // 2

            if mi*mi == x:
                return mi
            
            if mi*mi < x:
                lo = mi + 1
                result = mi
            else:
                hi = mi - 1

        return result


def main() -> None:
    solution = Solution()
    print(f"MySqrt(4) == 2 ? {solution.mySqrt(4) == 2}")
    print(f"MySqrt(8) == 2 ? {solution.mySqrt(8) == 2}")
    print(f"MySqrt(25) == 5 ? {solution.mySqrt(8) == 2}")

if __name__ == "__main__":
    main()