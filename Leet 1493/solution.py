class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        Finds the length of the longest subarray containing only 1s after deleting exactly one element from the input array.
        Args:
            nums (list[int]): A list of integers containing only 0s and 1s.
        Returns:
            int: The length of the longest subarray of 1s after deleting one element.
        Note:
            - If the array contains only 1s, the result will be len(nums) - 1.
            - Uses a sliding window approach to maintain at most one zero in the window.
        """
        n: int = len(nums)
        z_count: int = 0
        max_length: int = 0

        left: int = 0
        for right in range(n):
            if nums[right] == 0:
                z_count += 1

            while z_count > 1:
                if nums[left] == 0:
                    z_count -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length - 1


def main() -> None:
    print("1493. Longest Subarray of 1's After Deleting One Element")

    sol = Solution()
    
    print(f"case 1 should equal 3 ? {sol.longestSubarray(nums=[1,1,0,1])}")
    print(f"case 2 should equal 5 ? {sol.longestSubarray(nums=[0,1,1,1,0,1,1,0,1])}")
    print(f"case 3 should equal 2 ? {sol.longestSubarray(nums=[1,1,1])}")
    print(f"case 4 should equal 0 ? {sol.longestSubarray(nums=[1])}")


if __name__ == "__main__":
    main()