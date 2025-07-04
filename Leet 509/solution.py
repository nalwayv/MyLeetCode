class Solution:
    """
    The Fibonacci numbers, 
    
    commonly denoted F(n) form a sequence, 
    
    called the Fibonacci sequence, 
    
    such that each number is the sum of the two preceding ones, 
    
    starting from 0 and 1. That is,
    """
    @staticmethod
    def _calculate_fib(n: int, memo: dict[int, int]) -> int:
        if n < 2:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = Solution._calculate_fib(n-1, memo) + Solution._calculate_fib(n-2, memo)
        return memo[n]
        

    def fib_memo(self, n: int) -> int:
        memo: dict[int, int]  = {}
        return Solution._calculate_fib(n, memo)


    def fib_bottom_up(self, n: int) -> int:
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        n1: int = 1
        n2: int = 1
        
        for _ in range(2, n):
            n1, n2 = n2, n1 + n2
        
        return n2
    

def main() -> None:
    sol = Solution()
    case1 = sol.fib_memo(10)
    print(case1)
    print(f"case1 {"pass" if case1 == 55 else "fail"}")


if __name__ == "__main__":
    main()