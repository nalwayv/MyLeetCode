class Solution:
    """
    The Fibonacci numbers, 
    
    commonly denoted F(n) form a sequence, 
    
    called the Fibonacci sequence, 
    
    such that each number is the sum of the two preceding ones, 
    
    starting from 0 and 1. That is,
    """
    def fib(self, n: int) -> int:
        
        def recursive(n: int, cache: dict[int, int]) -> int:
            if n < 2:
                return n
            
            if n in cache:
                return cache[n]
        
            result: int = recursive(n-1, cache) + recursive(n-2, cache)
            cache[n] = result
            
            return result
        
        cache: dict[int, int]  = {}
        return recursive(n, cache)
