class Solution:
    def _get_trib(self, n: int, memo: dict[int, int]) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        if n in memo:
            return memo[n]
        
        result: int = self._get_trib(n-1, memo) + self._get_trib(n-2, memo) + self._get_trib(n-3, memo)
        memo[n] = result
        
        return result

    def tribonacci(self, n: int) -> int:
        memo: dict[int, int] = {}
        return self._get_trib(n, memo)
    

def main() -> None:
    print("1137. N-th Tribonacci Number")

    sol = Solution()

    case1: int = sol.tribonacci(4)
    print(f"case 1 trib(4) {'pass' if case1 == 4 else 'fail'}")
    
    case2: int = sol.tribonacci(25)
    print(f"case 2 trib(25){'pass' if case2 == 1389537 else 'fail'}")


if __name__ == "__main__":
    main()