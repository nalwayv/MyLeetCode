class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        i:int = 1
        j:int = 0

        sums: list[int] = []

        while i <= n:
            sums.append(sum(nums[j:i]))
            if i == n:
                j += 1
                i = j
            i+=1

        sums.sort()
        
        return sum(sums[left-1:right]) % 1000000007