class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1: int = 0
        p2: int = len(s) - 1
        while p1 < p2:
            s[p1],s[p2] = s[p2],s[p1]
            p1 += 1
            p2 -= 1

    def reverseStringR(self, s: list[str]) -> None:
        def reverse(p1: int, p2: int, s: list[str]) -> None:
            if p1 >= p2:
                return
            
            s[p1], s[p2] = s[p2], s[p1]
            reverse(p1+1, p2-1, s)
        
        reverse(0, len(s)-1, s)
        

def main() -> None:
    solution = Solution()

    s1: list[str] = ["h","e","l","l","o"]
    print(f"Input: {s1}")
    solution.reverseStringR(s1)
    print(f"Output: {s1}")

    s2: list[str] = ["H","a","n","n","a","h"]
    print(f"Input: {s2}")
    solution.reverseStringR(s2)
    print(f"Output: {s2}")    


if __name__ == "__main__":
    main()