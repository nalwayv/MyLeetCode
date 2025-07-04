class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        abc: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table: dict[str, int] = {abc[i]: i+1 for i in range(26)}
        n: int = len(columnTitle)
        
        result: int = 0
        for i, ch in enumerate(columnTitle):
            result += pow(26, n-i-1) * table[ch]

        return result


def main() -> None:
    print("171. Excel Sheet Column Number")

    sol = Solution()
    
    inputs: list[tuple[str,int]] = [
        ("A", 1),
        ("AB", 28),
        ("AZ", 52),
        ("ZY", 701),
        ("RFU", 12345),
        ("FXSHRXW", 2147483647),
    ]

    for input,answer in inputs:
        result: int = sol.titleToNumber(input)
        print(f"{result} == {answer}")


if __name__ == "__main__":
    main()