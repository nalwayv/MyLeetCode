class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result: list[str] = []
        n: int = len(nums)
        j: int = 0

        for i in range(1, n):
            diff: int = nums[i] - nums[i-1]
            if diff > 1:
                if nums[j] == nums[i - 1]:
                    result.append(f"{nums[j]}")
                else:
                    result.append(f"{nums[j]}->{nums[i - 1]}")
                j = i

        if j < n:
            if nums[j] == nums[n - 1]:
                result.append(f"{nums[j]}")
            else:
                result.append(f"{nums[j]}->{nums[n - 1]}")

        return result


def main() -> None:
    print("228. Summary Ranges")
    
    sol = Solution()
    # [0,2] --> "0->2"
    # [4,5] --> "4->5"
    # [7,7] --> "7"
    result: list[str] = sol.summaryRanges([0,1,2,4,5,7])
    print(result)

    # [0,0] --> "0"
    # [2,4] --> "2->4"
    # [6,6] --> "6"
    # [8,9] --> "8->9"
    result2: list[str] = sol.summaryRanges([0,2,3,4,6,8,9])
    print(result2)

    result3: list[str] = sol.summaryRanges([0,1,2,4,5,6,8,9,10,12, 14])
    print(result3)


if __name__ == "__main__":
    main()