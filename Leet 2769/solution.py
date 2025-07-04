class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


def main() -> None:
    print("2769. Find the Maximum Achievable Number")

    sol = Solution()
    
    print(sol.theMaximumAchievableX(4, 1))
    print(sol.theMaximumAchievableX(3, 2))


if __name__ == "__main__":
    main()