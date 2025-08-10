from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        
        digits = Counter(str(n))
        for i in range(31):
            if Counter(str(1 << i)) == digits:
                return True
        
        return False


def main() -> None:
    print("869. Reordered Power of 2")

    sol = Solution()
    
    print(sol.reorderedPowerOf2(1))
    print(sol.reorderedPowerOf2(10))


if __name__ == "__main__":
    main()
