class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen: set[int] = set()
        sub_sum: int = 0
        max_sum: int = 0
        n: int = len(nums)

        lo: int = 0
        for hi in range(n):
            while nums[hi] in seen:
                seen.remove(nums[lo])
                sub_sum -= nums[lo]
                lo += 1

            seen.add(nums[hi])
            sub_sum += nums[hi]
            max_sum = max(max_sum, sub_sum)

        return max_sum


def main() -> None:
    print("1695. Maximum Erasure Value")

    sol = Solution()

    print(sol.maximumUniqueSubarray(nums= [4,2,4,5,6]), 17, sep= " == ")
    print(sol.maximumUniqueSubarray(nums= [5,2,1,2,5,2,1,2,5]), 8, sep=" == ")


if __name__ == "__main__":
    main()