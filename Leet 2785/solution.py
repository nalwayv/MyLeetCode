class Solution:
    def sortVowels(self, s: str) -> str:
        result: list[str] = [c for c in s]


        vowels: list[str] = []
        idxs: list[int] = []
        for idx, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                vowels.append(ch)
                idxs.append(idx)

        vowels.sort()

        for i, v in zip(idxs, vowels):
            result[i] = v

        return "".join(result)
    

def main() -> None:
    print("2785. Sort Vowels in a String")

    sol = Solution()
    
    result: str = sol.sortVowels(s="lEetcOde")
    print(result)


if __name__ == "__main__":
    main()