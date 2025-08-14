class Solution:
    def bk(self, count: list[int], s: list[str], vowels: str, n: int):
        if n == 0:
            count[0] += 1
            return
        
        for v in vowels:
            if s and v >= s[-1]:
                s.append(v)
                self.bk(count, s, vowels, n-1)
                s.pop()

    def countVowelStrings(self, n: int) -> int:
        if n == 0:
            return -1
        
        if n == 1:
            return 5

        count = [0]
        self.bk(count, ["a"], "aeiou", n)
        return count[0]


def main() -> None:
    print("1641. Count Sorted Vowel Strings")

    sol = Solution()
    
    print(sol.countVowelStrings(2))
    print(sol.countVowelStrings(33))


if __name__ == "__main__":
    main()
