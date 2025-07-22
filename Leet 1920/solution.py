class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[num] for num in nums]
    

def main() -> None:
    print("1920. Build Array from Permutation")
    sol = Solution()
    print(sol.buildArray(nums=[0,2,1,5,3,4]))


if __name__ == "__main__":
    main()