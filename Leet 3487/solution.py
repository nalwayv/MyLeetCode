class Solution:
    def maxSum(self, nums: list[int]) -> int:
        n: int = len(nums)
        if n == 1:
            return nums[0]
        
        max_value: int = max(nums)
        if max_value <= 0:
            return max_value

        max_sum: int = 0
        seen: set[int] = set()
        lo: int = 0
        current_sum: int = 0

        for hi in range(n):
            while nums[hi] in seen:
                seen.remove(nums[lo])

                current_sum -= nums[lo]
            
            lo += 1

            if nums[hi] >= 0:
                current_sum += nums[hi]
                seen.add(nums[hi])

            max_sum = max(max_sum, current_sum)

        return max_sum
    

def main() -> None:
    print("3487. Maximum Unique Subarray Sum After Deletion")
    
    sol = Solution()

    print(sol.maxSum(nums=[1,2,3,4,5]), 15, sep=" == ")
    print(sol.maxSum(nums=[1,1,0,1,1]), 1, sep=" == ")
    print(sol.maxSum(nums=[-17, -15]), -15, sep=" == ")


if __name__ == "__main__":
    main()
