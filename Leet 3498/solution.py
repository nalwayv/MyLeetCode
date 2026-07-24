class Solution:
    def reverseDegree(self, s: str) -> int:
        result: int = 0
        for idx, ch in enumerate(s, start = 1):
            rev_idx: int = 26 - (ord(ch) - 97)
            result += rev_idx * idx
        return result


def main() -> None:
    print("3498. Reverse Degree of a String")
    s = Solution()
    result: int = s.reverseDegree("abc")
    print(result)


if __name__ == "__main__":
    main()