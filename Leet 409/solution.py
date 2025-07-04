from collections import Counter

class Solution:
    def is_even(self, n: int) -> bool:
        return (n ^ 1) == (n + 1)

    def longestPalindrome(self, s: str) -> int:        
        table: Counter[str] = Counter(s)

        n:int = len(s)
        odd_number_count: int = 0
        for val in table.values():
            if not self.is_even(val):
                odd_number_count += 1

        return (n - odd_number_count) + 1 if odd_number_count > 0 else n
    

def case_1(sol: Solution) -> None:
    letters: str = "abccccdd"
    result: int = sol.longestPalindrome(letters)
    print(f"Case 1: {result} == 7")


def case_2(sol: Solution) -> None:
    letters: str = "a"
    result: int = sol.longestPalindrome(letters)
    print(f"Case 2: {result} == 1")


def main() -> None:
    print("409. Longest Palindrome")

    sol = Solution()

    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()