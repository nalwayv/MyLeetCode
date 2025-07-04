class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        """
        Given an array of ints count valid ways to split if the following is true.
        
        - The sum if the first i+1 values is greater than or equal to the sum of the last n-i-1 values

        Args:
            nums (list[int]): valid list of ints

        Returns:
            int: number of valid ways to split
        """
        n: int = len(nums)

        # prefix sum 0 -> n
        left: list[int] = [0] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = left[i-1] + nums[i]

        # prefix sum n-1 -> 0
        right: list[int] = [0] * n
        right[0] = nums[n-1]
        for i in range(1, n):
            right[i] = right[i-1] + nums[n-i-1]

        count: int = 0
        for i in range(1, n):
            if left[i-1] >= right[n-i-1]:
                count += 1

        return count


def case1(sol: Solution) -> None:
    nums: list[int] = [10, 4, -8, 7]
    result:int = sol.waysToSplitArray(nums)
    print(f"Case1: {result}")


def case2(sol: Solution) -> None:
    nums: list[int] = [2,3,1,0]
    result:int = sol.waysToSplitArray(nums)
    print(f"Case2: {result}")


def main() -> None:
    print("2270. Number of Ways to Split Array")

    sol = Solution()
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()        