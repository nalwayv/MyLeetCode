class Solution:
    """
    You are given an integer array nums where the largest integer is unique.

    Determine whether the largest element in the array is at least twice as much as every other number in the array. 
    
    If it is, return the index of the largest element, or return -1 otherwise.
    
    Example:

        Input: nums = [3,6,1,0]

        output: 1

    """
    def dominantIndex(self, nums: list[int]) -> int:
        # GET MAX AND ITS INDEX
        result: int = 0
        max_num: int = -1
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                result = i

        # CHECK IT AGAINS OTHER EXCEPT ITSELF
        for i, num in enumerate(nums):
            if i != result:
                if num*2 > max_num:
                    return -1
        return result
    
def main() -> None:
    solution = Solution()
    print(f"Output: {solution.dominantIndex([3,6,1,0])}")
    print(f"Output: {solution.dominantIndex([1,2,3,4])}")


if __name__ == "__main__":
    main()