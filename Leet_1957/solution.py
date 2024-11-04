class Solution:
    def makeFancyString(self, s: str) -> str:
        """Convert string into a fancy string that is a string where no three consecutive characters are equal.

        Args:
            s (string): create a fancy string from this
        
        Returns:
            a fancy copy of s

        Example:
        >>> not_fancy: str = "aaabbbccc"
        >>> fancy: str = makeFancyString(not_fancy)
        """
        p1: int = 0
        p2: int = 0
        n: int = len(s)

        result: list[str] = []

        while p1 < n:
            p2 = p1
            while p2 < n and s[p1] == s[p2]:
                p2 += 1

            if (p2 - p1) >= 2:
                for _ in range(2):
                    result.append(s[p1])
            else:
                result.append(s[p1])

            p1 = p2

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