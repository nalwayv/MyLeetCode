class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels: list[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s2: list[str] = [chr for chr in s]

        p1: int = 0
        p2: int = len(s) - 1

        while p1 < p2:
            while p1 < p2 and s[p1] not in vowels:
                p1 += 1

            while p2 > p1 and s[p2] not in vowels:
                p2 -= 1

            if p1 < p2:
                s2[p1], s2[p2] = s2[p2], s2[p1]
                
                p1 += 1
                p2 -= 1

        return "".join(s2)
    

def main() -> None:
    print("345. Reverse Vowels of a String")
    sol = Solution()
    print(sol.reverseVowels("hello"))


if __name__ == "__main__":
    main()