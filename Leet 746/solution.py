# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def _climb(self, cost: list[int], i: int, memo: dict[int, int]) -> int:
        if i >= len(cost):
            return 0
        
        if i in memo:
            return memo[i]

        one_step: int = self._climb(cost, i+1, memo)
        two_step: int = self._climb(cost, i+2, memo)
        memo[i] = cost[i] + min(one_step, two_step)

        return memo[i]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo: dict[int, int] = {}
        
        one_step: int = self._climb(cost, 0, memo)
        two_step: int = self._climb(cost, 1, memo)
        
        return min(one_step, two_step)


def case1(sol: Solution) -> None:
    cost: list[int] = [10,15,20]
    result: int = sol.minCostClimbingStairs(cost)
    print(f"Case 1: {"pass" if result == 15 else "fail"}")


def case2(sol: Solution) -> None:
    cost: list[int] = [1,100,1,1,1,100,1,1,100,1]
    result: int = sol.minCostClimbingStairs(cost)
    print(f"Case 2: {"pass" if result == 6 else "fail"}")


def main() -> None:
    print("746. Min Cost Climbing Stairs")

    sol = Solution()

    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()