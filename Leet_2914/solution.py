class Solution:
    def minChanges(self, s: str) -> int:
        """Return minimum number of changes required to make the string s beautiful.

        A string is beautiful if it's possible to partition it into one or more substrings such that:
        - Each substring has an even length.
        - Each substring contains only 1's or only 0's.

        Args:
            s (string): an even length string of a binary number
            
        Example:
        >>> minChanges("1001")

        Returns:
            minimum count        
        """
        #is even?
        n: int = len(s)
        if (n ^ 1) != (n + 1):
            return 0
        
        count: int = 0
        for i in range(0, n, 2):
            #can partition?
            if (s[i] == "1" and s[i + 1] == "0") or (s[i] == "0" and s[i + 1] == "1"):
                count += 1

        return count


def case1(solution: Solution) -> None:
    test_case: bool = solution.minChanges("1001") == 2
    print(f"case 1: { "pass" if test_case else "fail" }")


def case2(solution: Solution) -> None:
    test_case: bool = solution.minChanges("10") == 1
    print(f"case 2: { "pass" if test_case else "fail" }")


def case3(solution: Solution) -> None:
    test_case: bool = solution.minChanges("0000") == 0
    print(f"case 3: { "pass" if test_case else "fail" }")

 
def main() -> None:
    print("2914. Minimum Number of Changes to Make Binary String Beautiful")

    solution = Solution()

    case1(solution)
    case2(solution)
    case3(solution)


if __name__ == "__main__":
    main()
