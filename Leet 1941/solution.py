class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n: int = len(s)
        table: dict[str, int] = {}
        occ: int = 1

        for i in range(n):
            if s[i] in table:
                table[s[i]] += 1
                occ = max(occ, table[s[i]])
            else:
                table[s[i]] = 1

        for i in range(n):
            if table[s[i]] != occ:
                return False
        return True
        

def main() -> None:
    print("1941. Check if All Characters Have Equal Number of Occurrences")

    sol = Solution()
    
    print(sol.areOccurrencesEqual("abacbc"))
    print(sol.areOccurrencesEqual("aaabb"))


if __name__ =="__main__":
    main()