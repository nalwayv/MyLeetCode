class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # for negative numbers
        if num < 0:
            num = num & ((1<<32)-1)

        table: str = "0123456789abcdef"
        result: list[str] = []

        while num > 0:
            remainder: int = num % 16
            result.insert(0, table[remainder])
            num //= 16

        return "".join(result)


def main() -> None:
    print("405. Convert a Number to Hexadecimal")

    sol = Solution()
    
    print(f"{sol.toHex(26)}")
    print(f"{sol.toHex(-1)}")
    print(f"{sol.toHex(2147483647)}")
    print(f"{sol.toHex(-2147483647)}")


if __name__ == "__main__":
    main()