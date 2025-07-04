class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s: int = len(s)
        len_t: int = len(t)
        
        if (len_s == 0 and len_t == 0) or len_s == 0:
            return True
                
        if len_s > len_t:
            return False

        # use p1 and p2 for 't' and p3 for 's'
        p1: int = 0
        p2: int = 0
        p3: int = 0

        while p1 < len_t:
            p2 = p1

            # skip over characters until next in 's' sequence is found or out of range
            while p2 < len_t and t[p2] != s[p3]:
                p2 += 1

            if p2 < len_t and t[p2] == s[p3]:
                p3 += 1
                if p3 == len_s:
                    return True

            p1 = p2 + 1

        return False


def main() -> None:
    print("392. Is Subsequence")
    
    sol = Solution()              

    print(f"case1 { "pass" if sol.isSubsequence("abc", "ahbgdc") else "fail" }")
    print(f"case2 { "pass" if not sol.isSubsequence("axc", "ahbgdc") else "fail" }")
    print(f"case3 { "pass" if sol.isSubsequence("", "") else "fail" }")
    print(f"case4 { "pass" if not sol.isSubsequence("ab", "a") else "fail" }")
    print(f"case5 { "pass" if sol.isSubsequence("", "ahbgdc") else "fail" }")


if __name__ == "__main__":
    main()
