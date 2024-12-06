class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        """Given a string `s` and a list if index to place spaces
        constructs a new string where a space is places at that index

        Example:
        >>> addSpaces('icodeinpython', [1,5,7,9]) == "i code in py thon"
        """
        builder: list[str] = []
        k: int = 0
        for j, chr in enumerate(s):
            if k < len(spaces) and j == spaces[k]:
                builder.append(" ")
                k += 1
            builder.append(chr)
        return "".join(builder)


def main() -> None:
    print("2109. Adding Spaces to a String")

    sol = Solution()

    result1 = sol.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15])
    print(result1 ==  "Leetcode Helps Me Learn")
        
    result2 = sol.addSpaces("icodeinpython", [1,5,7,9])
    print(result2 == "i code in py thon")

    result3 = sol.addSpaces("spacing", [0,1,2,3,4,5,6])
    print(result3 ==  " s p a c i n g")


if __name__ == "__main__":
    main()