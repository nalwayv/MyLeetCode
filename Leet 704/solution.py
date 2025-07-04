class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        lo:int = 0
        hi:int = len(nums) - 1
            
        while lo <= hi:
            mi: int = (lo + hi) // 2
            
            if nums[mi] == target:
                return mi
            
            if nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi - 1

        return -1


def main() -> None:
    print("704. Binary Search")
    sol = Solution()
    target: int = 9
    nums: list[int] = [-1, 0, 3, 5, 9, 12]
    print(f"nums={nums} search({target}) is as position ? {sol.search(nums, target)}")


if __name__ == "__main__":
    main()