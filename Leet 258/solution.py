class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum_total: int = 0

            # break down
            while num > 0:
                div, mod = divmod(num, 10)
                sum_total += mod
                num = div
            
            num += sum_total

        return num


def main() -> None:
    print("258. Add Digits")

    sol = Solution()
    
    print(f"case 1: {"pass" if sol.addDigits(38) == 2 else "fail"}")
    print(f"case 2: {"pass" if sol.addDigits(0) == 0 else "fail"}")
    print(f"case 3: {"pass" if sol.addDigits(43) == 7 else "fail"}")
    print(f"case 4: {"pass" if sol.addDigits(2147483647) == 1 else "fail"}")


if __name__ == "__main__":
    main()