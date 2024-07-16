class Solution:
    """
    Given two binary strings a and b, return their sum as a binary string.

    Example 1:
        Input: a = "11", b = "1"
        Output: "100"

    Example 2:
        Input: a = "1010", b = "1011"
        Output: "10101"

    """
    def binary_to_int(self, binary: str) -> int:
        result: int = 0
        for b in binary:
            result *= 2
            if b == '1':
                result += 1
        return result

    def int_to_binary(self, num: int) -> str:
        # get largest power of 2 that is less then num
        p1: int = 0
        p2: int = 1
        n: int = 0
        while p2 <= num:
            p1 = p2
            p2 *= 2
            n += 1
        
        # build out str table
        # example: ['1', '0', '1']
        result: list[str] = ['0'] * n
        at: int = 0
        while True:
            # only subtract if result is above zero
            if (num - p1) >= 0:
                num -= p1
                result[at] = '1'

            at += 1
            p1 //= 2

            if num <= 0:
                break

        return "".join(result)

    def addBinary(self, a: str, b: str) -> str:
        num: int = self.binary_to_int(a) + self.binary_to_int(b)
        return "0" if num == 0 else self.int_to_binary(num)


def main() -> None:
    solution = Solution()
    print(f"Output: {solution.addBinary("11", "1")}")
    print(f"Output: {solution.addBinary("0", "0")}")
    print(f"Output: {solution.addBinary("1010", "1011")}")


if __name__ == "__main__":
    main()