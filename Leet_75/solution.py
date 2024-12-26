class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n: int = len(nums)
        for i in range(1, n):

            curr: int = i
            # sort to the left of current
            while curr and nums[curr-1] > nums[curr]:
                nums[curr], nums[curr-1] = nums[curr-1], nums[curr]
                curr-=1


def main() -> None:
    print("75. Sort Colors")
    
    sol = Solution()

    nums = [2,0,2,1,1,0]
    print(f"Before: {nums}")
    sol.sortColors(nums)
    print(f"After: {nums}")


if __name__ == "__main__":
    main()