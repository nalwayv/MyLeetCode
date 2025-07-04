class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo: int = 1
        hi: int = num
        while lo <= hi:
            m: int = (lo + hi) // 2
            sq: int = m * m
            
            if sq == num:
                return True
            
            if sq < num:
                lo = m + 1
            else:
                hi = m - 1
            
        return False
    

def main() -> None:
    print("367. Valid Perfect Square")
    
    sol = Solution()
    print(sol.isPerfectSquare(16))
    print(sol.isPerfectSquare(14))


if __name__ == "__main__":
    main()