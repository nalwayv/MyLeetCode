import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        values: list[tuple[int, int]] = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(values)

        for _ in range(k):
            current, i = heapq.heappop(values)

            current *= multiplier
            nums[i] = current

            heapq.heappush(values, (current, i))

        return nums


def case1(sol: Solution) -> None:
    nums: list[int] = [2,1,3,5,6]
    k = 5
    m = 2
    result = sol.getFinalState(nums, k, m)
    print(f"Case 1: {result}")


def case2(sol: Solution) -> None:
    nums: list[int] = [1, 2]
    k = 3
    m = 4
    result = sol.getFinalState(nums, k, m)
    print(f"Case 2: {result}")


def case3(sol: Solution) -> None:
    nums: list[int] = [2, 2]
    k = 1
    m = 5
    result = sol.getFinalState(nums, k, m)
    print(f"Case 3: {result}")


def main() -> None:
    print("3264. Final Array State After K Multiplication Operations I")

    sol = Solution()
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()
