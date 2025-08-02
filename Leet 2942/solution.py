class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i, word in enumerate(words) if x in word]


def main() -> None:
    print("2942. Find Words Containing Character")

    result: list[int] = Solution().findWordsContaining(words=["leet", "code"], x='e')
    print(result)


if __name__ == "__main__":
    main()
