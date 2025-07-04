class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val: int = max(nums)
        max_sub: int = -1
        
        counter: int = 0
        for num in nums:
            if num == max_val:
                counter += 1
            else:
                counter = 0
            max_sub = max(counter, max_sub)
        return max_sub


def main() -> None:
    print("2419. Longest Subarray With Maximum Bitwise AND")
    sol = Solution()

    print(f"case 1: {sol.longestSubarray([1,2,3,3,2,2]) == 2}")
    print(f"case 2: {sol.longestSubarray([1,2,3,4]) == 1}")
    print(f"case 3: {sol.longestSubarray([1]) == 1}")
    print(f"case 4: {sol.longestSubarray([1,1,1,1,1,1,1,1]) == 8}")
    print(f"case 5: {sol.longestSubarray([1,1,1,2,2,1]) == 2}")
    print(f"case 5: {sol.longestSubarray([1,1,1,2,1]) == 1}")


if __name__ == "__main__":
    main()