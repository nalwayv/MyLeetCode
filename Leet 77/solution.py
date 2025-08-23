from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return [[*c] for c in combinations(range(1, n+1), k)]


def main() -> None:
    print("77. Combinations")
    sol = Solution()

    print("case 1")
    print(sol.combine(n=4, k=2))

    print("case 2")
    print(sol.combine(n=1, k=1))


if __name__ == "__main__":
    main()