class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n: int = len(nums)
        lo: int = -1
        for i in range(n):
            lo = i
            
            # get next smallest value to the right of current
            for j in range(i + 1, n):
                if nums[j] < nums[lo]:
                    lo = j
            # swap
            nums[lo], nums[i] = nums[i], nums[lo]


def main() -> None:
    print("75. Sort Colors")
    
    sol = Solution()

    nums = [2,0,2,1,1,0]
    print(f"Before: {nums}")
    sol.sortColors(nums)
    print(f"After: {nums}")


if __name__ == "__main__":
    main()