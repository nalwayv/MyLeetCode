class Solution:
    def __init__(self) -> None:
        self.table: dict[str, int] = {}

        ascii: str = "abcdefghijklmnopqrstuvwxyz"
        i: int = 1
        for chr in ascii:
            self.table[chr] = i
            i += 1

    def getLucky2(self, s: str, k: int) -> int:
        stk: list[int] = []
        for c in s:
            num: int = self.table[c]
            while num > 0:
                stk.append(num % 10)
                num //= 10

        number: int = -1

        for _ in range(k):

            # sum from stack

            curr: int = 0
            while stk:
                curr += stk.pop()

            # prevent repeating
            
            if curr == number:
                return number

            number = curr

            # break down and add back to stack

            while curr > 0:
                stk.append(curr % 10)
                curr //= 10
            
        return number


def main() -> None:
    #              str | k |                    to int | result
    #                 -+- -+-                         -+-
    #              iii | 1 |                      9999 | 36
    #         leetcode | 2 |               12552031545 | 6
    #             zbax | 2 |                    262124 | 8
    # hvmhoasabaymnmsd | 1 | 8223185119112152314131914 | 79

    print("1945. Sum of Digits of String After Convert")

    sol = Solution()

    print(f"case 1 { 'pass' if sol.getLucky2("iiii", 1) == 36 else 'fail' }")
    print(f"case 2 { 'pass' if sol.getLucky2("leetcode", 2) == 6 else 'fail' }")
    print(f"case 3 { 'pass' if sol.getLucky2("zbax", 2) == 8 else 'fail' }")
    print(f"case 4 { 'pass' if sol.getLucky2("hvmhoasabaymnmsd", 1) == 79 else 'fail' }")


if __name__ == "__main__":
    main()

