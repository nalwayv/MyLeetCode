class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Calculates the number of pairs (i, j) such that 1 <= i <= n, 1 <= j <= m, and (i + j) is odd.

        Args:
            n (int): The upper bound for i (inclusive).
            m (int): The upper bound for j (inclusive).

        Returns:
            int: The count of pairs (i, j) where the sum (i + j) is odd.
        """
        odd_n: int = n // 2
        even_n: int = n - odd_n
        odd_m: int = m // 2
        even_m: int = m - odd_m
        
        return (odd_n * even_m) + (odd_m * even_n)
    

def main() -> None:
    print("3021. Alice and Bob Playing Flower Game")
    sol = Solution()
    
    case1: int = sol.flowerGame(n=3, m=2)
    print(f"case 1 should equal 3 ? {case1}")

    case2: int = sol.flowerGame(n=1, m=1)
    print(f"case 2 should equal 0 ? {case2}")
    

if __name__ == "__main__":
    main()