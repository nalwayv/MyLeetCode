class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words: list[str] = s.strip().split()
        return len(words[-1])


def main() -> None:
    print("58. Length of Last Word")

    sol = Solution()
    
    print(sol.lengthOfLastWord("Hello World"))
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))
    print(sol.lengthOfLastWord("luffy is still joyboy"))


if __name__ == "__main__":
    main()