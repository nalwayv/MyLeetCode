class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_val: int = -1
        length: int = len(num)
        i: int = 0
        for j in range(length):
            if num[i] != num[j]:
                i = j

            if j - i >= 2:
                max_val = max(max_val, int(num[i]))

        if max_val == -1:
            return ""
        return str(max_val) * 3


def main() -> None:
    print("2264. Largest 3-Same-Digit Number in String")
    
    sol = Solution()

    print(sol.largestGoodInteger("6777133339"))
    print(sol.largestGoodInteger("2300019"))
    print(sol.largestGoodInteger("42352338"))


if __name__ == "__main__":
    main()