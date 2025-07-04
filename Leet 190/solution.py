class Solution:
    def reverseBits(self, n: int) -> int:
        #using format to get a 32 bit length str because bin() removes zeros
        str_bin_format: str = "{:032b}".format(n)
        result: int = 0
        length: int = 32
        for i in range(length-1, -1, -1):
            result *= 2
            if str_bin_format[i] == '1':
                result += 1
        return result


def main() -> None:
    print("190. Reverse Bits")

    solution = Solution()

    n1: int = 0b00000010100101000001111010011100
    case_1: bool = solution.reverseBits(n1) == 964176192
    print(f"case 1: {"pass" if case_1 else "fail"}")

    n2: int = 0b11111111111111111111111111111101
    case_2: bool = solution.reverseBits(n2) == 3221225471
    print(f"case 1: {"pass" if case_2 else "fail"}")


if __name__ == "__main__":
    main()