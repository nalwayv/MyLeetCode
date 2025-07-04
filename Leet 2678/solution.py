class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count: int = 0
        for d in details:
            if int(d[11]) * 10 + int(d[12]) > 60:
                count += 1
        return count


def main() -> None:
    print("2678. Number of Senior Citizens")
    sol = Solution()
    count: int = sol.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"])
    print(count)


if __name__ == "__main__":
    main()