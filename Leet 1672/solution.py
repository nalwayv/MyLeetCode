# Richest Customer Wealth
#
# Sum the total amount and return the largest
#
#    a  b  c
# a [1, 2, 3] = 6
# b [3, 3, 3] = 9  <- largest
# c [2, 1, 4] = 7
#

CASE_1: list[list[int]] = [[1, 2, 3], [3, 2, 1]]
CASE_2: list[list[int]] = [[1, 5], [7, 3], [3, 5]]
CASE_3: list[list[int]] = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

RESULT_1: int = 6
RESULT_2: int = 10
RESULT_3: int = 17


def maximumWealth(accounts: list[list[int]]) -> int:
    # keep track of largest val
    max_wealth: int = -2147483648

    n1: int = len(accounts)
    for i in range(n1):
        wealth: int = sum(accounts[i])
        max_wealth: int = max(max_wealth, wealth)

    return max_wealth


def main() -> None:
    print(maximumWealth(CASE_1) == RESULT_1)
    print(maximumWealth(CASE_2) == RESULT_2)
    print(maximumWealth(CASE_3) == RESULT_3)


if __name__ == "__main__":
    main()