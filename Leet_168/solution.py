class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        abc: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n: int = len(abc)
        result: list[str] = []

        while columnNumber > 0:
            div, mod = divmod(columnNumber, n)
            columnNumber = div

            index: int = mod - 1
            if index < 0:
                result.insert(0, abc[n + index])
                columnNumber -= 1
            else:
                result.insert(0, abc[index])

        return "".join(result)


def main() -> None:
    print("168. Excel Sheet Column Title")

    sol = Solution()
    
    inputs: list[tuple[int,str]] = [
        (1, "A"),
        (27,"AA"),
        (28, "AB"),
        (52, "AZ"),
        (701, "ZY"),
        (12345,"RFU"),
        (2147483647,"FXSHRXW"),
    ]

    for input,answer in inputs:
        result: str = sol.convertToTitle(input)
        print(f"{result} == {answer}")


if __name__ == "__main__":
    main()