class Solution:
    def hammingWeight(self, n: int) -> int:
        count: int = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
        return count


def main() -> None:
    print("191. Number of 1 Bits")

    sol = Solution()
    
    print(f"case1: {"pass" if (sol.hammingWeight(11) == 3) else "fail"} ")
    print(f"case2: {"pass" if (sol.hammingWeight(128) == 1) else "fail"} ")
    print(f"case3: {"pass" if (sol.hammingWeight(2147483645) == 30) else "fail"} ")


if __name__ == "__main__":
    main()