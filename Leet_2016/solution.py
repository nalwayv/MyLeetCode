class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        n: int = len(nums)
        result: int = -1
        min_value: int = nums[0]
        for i in range(1, n):
            current: int = nums[i]
            if current <= min_value:
                min_value = current
            else:
                result = max(result, current - min_value)
        return result


def main() -> None:
    print("2016. Maximum Difference Between Increasing Elements")

    sol = Solution()
    
    print(sol.maximumDifference([7,1,5,4]), 4, sep= " = ")
    print(sol.maximumDifference([9,4,3,2]), -1, sep= " = ")
    print(sol.maximumDifference([1,5,2,10]), 9, sep= " = ")


if __name__ == "__main__":
    main()
        