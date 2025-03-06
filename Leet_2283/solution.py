class Solution:
    def digitCount(self, num: str) -> bool:
        table: dict[int, int] = {}

        for val in num:
            curr = int(val)
            if curr in table:
                table[curr] += 1
            else:
                table[curr] = 1
    
        n: int = len(num)
        result: str = ""
        for i in range(n):
            if i in table:
                result += str(table[i])
            else:
                result += "0"

        return result == num


def main() -> None:
    print("2283. Check if Number Has Equal Digit Count and Digit Value")

    sol = Solution()

    print(sol.digitCount("1210"))
    print(sol.digitCount("030"))
    print(sol.digitCount("123123123"))


if __name__ == "__main__":
    main()