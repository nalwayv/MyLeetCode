class Solution:
    """
    Given an integer array nums, rotate the array to the right by k steps,
    where k is non-negative.
    """
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # tmp array to store original 
        n: int = len(nums)
        result: list[int] = [0] * n
        for i,num in enumerate(nums):
            result[i] = num

        # using mod % to loop back
        j: int = (n - k) % n
        for i in range(n):
            nums[i] = result[j]
            j = (j+1) % n

        print(nums)


def main() -> None:
    solution = Solution()
    solution.rotate([1,2,3,4,5,6,7], 3)
    solution.rotate([-1,-100,3,99], 2)


if __name__ == "__main__":
    main()