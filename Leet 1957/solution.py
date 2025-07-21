class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Returns a 'fancy' version of the input string `s` where no three consecutive characters are the same.
        Args:
            s (str): The input string.
        Returns:
            str: The modified string with no three consecutive identical characters.
        """
        result: list[str] = []
        n: int = len(s)
        
        lo: int = 0
        for hi in range(n):
            if s[lo] != s[hi]:
                lo = hi

            if (hi - lo) < 2:
                result.append(s[lo])
                
        return "".join(result)


def main() -> None:
    print("1957. Delete Characters to Make Fancy String")

    sol = Solution()

    print(sol.makeFancyString("leeetcode"))
    print(sol.makeFancyString("aaabaaaa"))
    print(sol.makeFancyString("aab"))
    print(sol.makeFancyString("abbcccddddeeeee"))


if __name__ == "__main__":
    main()