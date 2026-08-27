from collections import Counter


def lexGreaterPermutation(s: str, target: str) -> str:
    frequency: Counter[str] = Counter(s)
    chars: list[str] = sorted(frequency)

    def solve(greater: bool, pos: int, ans: str) -> str:
        if greater:
            return ans + "".join(char * frequency[char] for char in chars)

        if pos == len(s):
            return ""

        for char in chars:
            if frequency[char] == 0 or char < target[pos]:
                continue

            frequency[char] -= 1
            result: str = solve(greater or char > target[pos], pos + 1, ans + char)
            frequency[char] += 1

            if result:
                return result

        return ""

    return solve(False, 0, "")


def test_case(s: str, t: str, e: str) -> None:
    res: str = "pass" if lexGreaterPermutation(s, t) == e else "fail"
    print(f"({s}, {t}) should equal {e} ? {res}")


def main() -> None:
    print("3720. Lexicographically Smallest Permutation Greater Than Target")

    test_case("abc", "bba", "bca")
    test_case("leet", "code", "eelt")
    test_case("baba", "bbaa", "")
    test_case("ab", "ab", "ba")
    test_case("z", "z", "")
    test_case("z", "a", "z")


if __name__ == "__main__":
    main()
