from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counter: Counter[str] = Counter()

        counter.update(s1.split())
        counter.update(s2.split())

        result: list[str] = []
        for word, count in counter.most_common():
            if count == 1:
                result.append(word)

        return result


def main() -> None:
    print("884. Uncommon Words from Two Sentences")
    
    sol = Solution()

    c1: list[str] = sol.uncommonFromSentences("this apple is sweet", "this apple is sour")
    c2: list[str] = sol.uncommonFromSentences("apple apple", "banana")

    print(c1)
    print(c2)


if __name__ == "__main__":
    main()