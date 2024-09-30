import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1: str = str1 + str2
        s2: str = str2 + str1

        if s1 != s2:
            return ""

        l1: int = len(str1)
        l2: int = len(str2)
        gcd: int = math.gcd(l1, l2)
        
        return s1[:gcd]


def main() -> None:
    sol = Solution()
    print(f"case1 { "pass" if sol.gcdOfStrings("ABCABC", "ABC") == "ABC" else "fail" }")


if __name__ == "__main__":
    main()