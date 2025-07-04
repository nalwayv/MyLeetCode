class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels: str = "aeiou"
        n: int = len(words)
        m: int = len(queries)

        # prefix count words that start end end in a vowel
        prefix: list[int] = [0] * n
        prefix[0] = 1 if (words[0][0] in vowels and words[0][-1] in vowels) else 0
        for i in range(1, n):
            curr: int = 1 if (words[i][0] in vowels and words[i][-1] in vowels) else 0
            prefix[i] = prefix[i-1] + curr
        
        result: list[int] = [0] * m
        for i in range(m):
            lo: int = queries[i][0]
            hi: int = queries[i][1]
            result[i] = prefix[hi] if lo <= 0 else prefix[hi] - prefix[lo-1]

        return result


def case1(sol: Solution) -> None:
    words: list[str] = ["aba","bcb","ece","aa","e"]
    queries: list[list[int]] = [[0,2], [1,4], [1,1]]
    result: list[int] = sol.vowelStrings(words, queries)
    print(f"Result: {result}")


def case2(sol: Solution) -> None:
    words: list[str] = ["a", "e", "i"]
    queries: list[list[int]] = [[0,2], [0,1], [2,2]]
    result: list[int] = sol.vowelStrings(words, queries)
    print(f"Result: {result}")


def main() -> None:
    print("2559. Count Vowel Strings in Ranges")

    sol = Solution()
    
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()