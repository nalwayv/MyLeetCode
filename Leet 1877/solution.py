class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        n: int = len(nums)
        
        result: int = -1
        for i in range(n // 2):
            result = max(result, nums[i] + nums[n - i - 1])

        return result
    

def main() -> None:
    print("1877. Minimize Maximum Pair Sum in Array")

    sol = Solution()
    
    print(sol.minPairSum([3,5,2,3]))
    print(sol.minPairSum([3,5,4,2,4,6]))


if __name__ == "__main__":
    main()