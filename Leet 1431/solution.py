class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n: int = len(candies)
        result: list[bool] = [False] * n
        max_candies: int = max(candies)

        for i, v in enumerate(candies):
            if v + extraCandies >= max_candies:
                result[i] = True

        return result
    

def case1(sol: Solution) -> None:
    candies = [2,3,5,1,3]
    extra = 3
    print(sol.kidsWithCandies(candies, extra))


def case2(sol: Solution) -> None:
    candies = [4,2,1,1,2]
    extra = 1
    print(sol.kidsWithCandies(candies, extra))


def case3(sol: Solution) -> None:
    candies = [12,1,12]
    extra = 10
    print(sol.kidsWithCandies(candies, extra))


def main() -> None:
    sol = Solution()
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    print("1431. Kids With the Greatest Number of Candies")
    main()