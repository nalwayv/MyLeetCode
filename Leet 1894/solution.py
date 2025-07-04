class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        sum_chalk: int = sum(chalk)
        while k >= sum_chalk:
            k = k % sum_chalk

        for i, c in enumerate(chalk):
            if c > k:
                return i
            k -= c

        return 0


def case1(sol :Solution) -> None:
    chalk: list[int] = [5,1,5]
    k: int = 22
    result: int = sol.chalkReplacer(chalk, k)
    test: str = "pass" if result == 0 else "fail"
    print(f"case 1 {test}")


def case2(sol :Solution) -> None:
    chalk: list[int] = [3,4,1,2]
    k: int = 25
    result: int = sol.chalkReplacer(chalk, k)
    test: str = "pass" if result == 1 else "fail"
    print(f"case 2 {test}")


def main() -> None:
    print("1894. Find the Student that Will Replace the Chalk")

    sol = Solution()
    
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()