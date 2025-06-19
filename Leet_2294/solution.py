class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        #NOTE: max - min has to be <= k

        nums.sort()

        n: int = len(nums)
        count: int = 0

        lo: int = 0
        hi: int = 0
        while lo < n:
            while hi < n and nums[hi] - nums[lo] <= k:
                hi += 1
            count += 1
            lo = hi    

        return count
        

def main() -> None:
    print("2294. Partition Array Such That Maximum Difference Is K")

    sol = Solution()
    
    print("Count: ", sol.partitionArray([3,6,1,2,5], 2))
    print("Count: ", sol.partitionArray([1,2,3], 1))
    print("Count: ", sol.partitionArray([2,2,4,5], 0))
    print("Count: ", sol.partitionArray([1,2,3,23,1,2,4,5,1,2], 4))


if __name__ == "__main__":
    main()
    
