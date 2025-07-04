class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table: dict[str, int] = {}

        for vs in s:
            if vs in table:
                table[vs] += 1
            else:
                table[vs] = 1

        for vt in t:
            if vt in table and table[vt] > 0:
                table[vt] -= 1
            else:
                table[vt] = 1

        for k,v in table.items():
            if v == 1:
                return k
            
        return ""


def main() -> None:
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))
    print(sol.findTheDifference("", "y"))
    print(sol.findTheDifference("a", "aa"))


if __name__ == "__main__":
    main()