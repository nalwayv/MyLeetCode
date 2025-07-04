class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """Given two strings s and goal, 
        return true if and only if s can 
        become goal after some number of shifts on s.

        Args:
            s (string): search this string.
            goal (string): if s after shifts can equal this string.

        Returns:
            True if s can become goal after n shifts on s.
        """
        n: int = len(s)
        #having a double of s helps with circular search
        #
        #goal:     cab
        #search: abcabc
        double_str: str = s + s

        for i in range(n):
            if goal == double_str[i:i+n]:
                return True
        return False
    

def main() -> None:
    print("796. Rotate String")

    sol = Solution()

    case_1: bool = sol.rotateString("abcde", "bcdea")
    print(f"case 1: { "pass" if case_1 else "fail" }")

    case_2: bool = sol.rotateString("abcde", "cdeab")
    print(f"case 2: { "pass" if case_2 else "fail" }")

    case_3: bool = sol.rotateString("abcde", "abced")
    print(f"case 3: { "pass" if not case_3 else "fail" }")


if __name__ == "__main__":
    main()
    
