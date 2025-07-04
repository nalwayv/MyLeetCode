class Solution:
    """
    Climbing Stairs.

    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. 
    
    In how many distinct ways can you climb to the top?
    """
    def climbStairs(self, n: int) -> int:
        def get_step(n: int, cache: dict[int, int]) -> int:
            if n <= 2:
                return n
            
            if n in cache:
                return cache[n]
            
            result = get_step(n-2, cache) + get_step(n-1, cache)
            cache[n] = result
            return result
        
        cache: dict[int, int] = {}
        return get_step(n, cache)