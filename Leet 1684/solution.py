
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        """
        main: set[str] = set()
        for allow in allowed:
            main.add(allow)

        count: int = len(words)
        other: set[str] = set()
        for word in words:
            for ch in word:
                if ch not in main:
                    other.add(ch)
            
            if len(other) > 0:
                count -= 1

            other.clear()

        return count


def case_1(sol: Solution) -> None:
    allowed: str = "ab"
    words: list[str] = ["ad","bd","aaab","baa","badab"]
    result: int = sol.countConsistentStrings(allowed, words)

    print(f"case 1 { 'pass' if result == 2 else 'fail' }")


def case_2(sol: Solution) -> None:
    allowed: str = "abc"
    words: list[str] = ["a","b","c","ab","ac","bc","abc"]
    result: int = sol.countConsistentStrings(allowed, words)

    print(f"case 2 { 'pass' if result == 7 else 'fail' }")


def case_3(sol: Solution) -> None:
    allowed: str = "cad"
    words: list[str] = ["cc","acd","b","ba","bac","bad","ac","d"]
    result: int = sol.countConsistentStrings(allowed, words)

    print(f"case 3 { 'pass' if result == 4 else 'fail' }")


def main() -> None:
    print("1684. Count the Number of Consistent Strings")
    
    sol = Solution()

    case_1(sol)
    case_2(sol)
    case_3(sol)


if __name__ == "__main__":
    main()
        