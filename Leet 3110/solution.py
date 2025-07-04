class Solution:
    def scoreOfString(self, s: str) -> int:
        result: int = 0
        n: int = len(s)
        
        for i in range(1, n):
            result += abs(ord(s[i-1]) - ord(s[i]))

        return result


def main() -> None:
    print("3110. Score of a String")

    sol = Solution()

    case1: int = sol.scoreOfString("hello")
    test1: str = "pass" if case1 == 13 else "fail"
    print(f"Case 1: {test1}")

    case2: int = sol.scoreOfString("zaz")
    test2: str = "pass" if case2 == 50 else "fail"
    print(f"Case 2: {test2}")


if __name__ == "__main__":
    main()