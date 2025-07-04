import math

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """
        Given an integer array nums, 
        return the maximum difference between two successive elements in its sorted form. 
        If the array contains less than two elements, 
        return 0.
        """
        n: int = len(nums)
        if n < 2:
            return 0
        
        max_gap: float = -math.inf
        sorted_nums: list[int] = sorted(nums)

        for i in range(1, n):
            gap: float = (sorted_nums[i] - sorted_nums[i-1])
            if gap > max_gap:
                max_gap = gap

        return int(max_gap)


def case1(sol: Solution) -> None:
    nums: list[int] = [3,6,9,1]
    result: int = sol.maximumGap(nums)
    print(f"Case1: {result} == 3")


def case2(sol: Solution) -> None:
    nums: list[int] = [10]
    result: int = sol.maximumGap(nums)
    print(f"Case2: {result} == 0")


def main() -> None:
    print("164. Maximum Gap")

    sol = Solution()
    
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()