class Solution:
    """
    2235. Add Two Integers
    """
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


def main() -> None:
    solution = Solution()
    case1: bool = solution.sum(12, 5) == 17
    case2: bool = solution.sum(-10, 4) == -6

    print(f"Case 1: {case1}")
    print(f"Case 2: {case2}")


if __name__ == "__main__":
    main()