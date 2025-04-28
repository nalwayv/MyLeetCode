class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        frequency: dict[str, int] = {}
        seperators: str = "!?',;. "

        result: str = ""
        max_frequency: int = 0

        lo: int = 0
        hi: int = len(paragraph)
        normalized: str = paragraph.lower()

        while lo < hi:
            curr: int = lo
            while curr < hi and normalized[curr] not in seperators:
                curr += 1

            if (curr - lo) > 0:
                word: str = normalized[lo:curr]

                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1

                if frequency[word] > max_frequency and word not in banned:
                    max_frequency = frequency[word]
                    result = word

            lo = curr + 1

        return result


# ** Test Cases **


def test_case(sol: Solution, paragraph: str, expected: str, banned: list[str]) -> None:
    result: str = sol.mostCommonWord(paragraph, banned)
    test_result: str = "pass" if result == expected else "fail"
    print(f"Result: {test_result}")


def case_1(sol: Solution) -> None:
    print("Case 1")
    paragraph: str = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned: list[str] = ["hit"]
    test_case(sol, paragraph, "ball", banned)


def case_2(sol: Solution) -> None:
    print("Case 2")
    paragraph: str = "a."
    banned: list[str] = []
    test_case(sol, paragraph, "a", banned)


# ** Main **


def main() -> None:
    print("819. Most Common Word")

    sol = Solution()
    
    case_1(sol)
    case_2(sol)


if __name__ == "__main__":
    main()