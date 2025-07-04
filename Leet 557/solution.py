class Solution:
    """
    Given a string s, reverse the order of characters in each word
    within a sentence while still preserving whitespace and initial word order.

    Example 1:
        Input: s = "Let's take LeetCode contest"
        Output: "s'teL ekat edoCteeL tsetnoc"

    Example 2:
        Input: s = "Mr Ding"
        Output: "rM gniD"
    """
    def reverseWords(self, s: str) -> str:
        words: list[str] = []
        result: str = ""
        n: int = len(s)
        p1: int = 0

        while p1 < n:
            p2: int  = p1
            while p2 < n and (s[p2].isascii() and not s[p2].isspace()):
                p2 += 1

            diff: int = p2 - p1
            if diff > 0:
                result += s[p1:p2][::-1]
                if p2 < n:
                    result += " "
                words.append(s[p1:p2][::-1])
            p1 = p2 + 1

        return " ".join(words)

    
def main() -> None:
    solution = Solution()
    print(f"Output: {solution.reverseWords("Let's take LeetCode contest")}")
    print(f"Output: {solution.reverseWords("Mr Ding")}")


if __name__ == "__main__":
    main()