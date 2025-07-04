class Solution:
    def brute_force(self, s: str, k: int) -> int:
        vowels: set[str] = {"a", "e", "i", "o", "u"}
        n: int = len(s)
        result: int = 0

        for i in range(n - k + 1):
            count: int = 0
            for j in range(k):
                if s[i+j] in vowels:
                    count += 1
            result = max(result, count)

        return result

    def maxVowels(self, s: str, k: int) -> int:
        n: int = len(s)
        vowels: list[str] = ['a', 'e', 'i', 'o', 'u']

        count: int = 0
        
        for i in range(k):
            if s[i] in vowels:
                count += 1

        result: int = count

        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            
            if s[i-k] in vowels:
                count -= 1
            
            result = max(result, count)

        return result


def main() -> None:
    print("1456. Maximum Number of Vowels in a Substring of Given Length")

    sol = Solution()
    
    print(f"case 1 {"pass" if sol.maxVowels("abciiidef", 3) == 3 else "fail"}")
    print(f"case 2 {"pass" if sol.maxVowels("aeiou", 2) == 2 else "fail"}")
    print(f"case 3 {"pass" if sol.maxVowels("leetcode", 3) == 2 else "fail"}")


if __name__ == "__main__":
    main()
