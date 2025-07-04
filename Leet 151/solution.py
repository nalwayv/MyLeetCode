class Solution:
    """
    Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.
    
    Example:
        Input: s = "the sky is blue"
        Output: "blue is sky the"
    """
    def reverseWords(self, s: str) -> str:
        words: list[str] = []
        n: int = len(s)
        end: int = n - 1
        p1: int = end

        # work backwords to avoid reversing result
        while p1 >= 0:
            p2: int = p1
            while p2 >= 0 and s[p2].isalnum():
                p2 -= 1
            
            diff: int = abs(p2 - p1)
            if diff > 0:
                start: int = p2 + 1
                words.append(s[start:start+diff])

            p1 = p2 - 1
    
        return " ".join(words)


def main() -> None:
    solution = Solution()
    print(f"Output: {solution.reverseWords("the sky is blue")}")
    print(f"Output: {solution.reverseWords("  hello world  ")}")
    print(f"Output: {solution.reverseWords("a good   example")}")
    print(f"Output: {solution.reverseWords("EPY2giL")}")


if __name__ == "__main__":
    main()