class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_count: int = 0

        for sentence in sentences:
            max_count = max(max_count, len(sentence.split(' ')))

        return max_count


def main() -> None:
    print("2114. Maximum Number of Words Found in Sentences")

    sol = Solution()
    
    case1: int = sol.mostWordsFound(sentences=["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
    print(f"case 1 should equal 6? {case1}")


if __name__ == "__main__":
    main()
        