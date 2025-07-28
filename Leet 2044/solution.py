class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        """
        """
        tally: dict[int, int] = {}
        n: int = len(nums)
        max_or: int = 0

        for i in range(1 << n):
            sum_or: int = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    sum_or |= nums[j]

            tally[sum_or] = tally.get(sum_or, 0) + 1
            max_or = max(max_or, sum_or)

        return tally[max_or]


def main() -> None:
    print("2044. Count Number of Maximum Bitwise-OR Subsets")

    sol = Solution()
    
    print(f"case 1 should equal 2 ?")
    print(sol.countMaxOrSubsets(nums=[3,1]), 2, sep=" == ")

    print(f"case 2 should equal 7 ?")
    print(sol.countMaxOrSubsets(nums=[2,2,2]), 7, sep=" == ")

    print(f"case 2 should equal 6 ?")
    print(sol.countMaxOrSubsets(nums=[3,2,1,5]), 6, sep=" == ")


if __name__ == "__main__":
    main()
        