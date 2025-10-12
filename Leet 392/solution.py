class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s: int = len(s)
        len_t: int = len(t)

        j: int = 0
        for i in range(len_t):
            # found match
            if j < len_s and s[j] == t[i]:
                j += 1

        return j == len_s or s == ''



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
