class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum: int = sum(nums)
        target: int = total_sum % p
        
        if target == 0:
            return 0
        
        seen: dict[int, int] = {0: -1}
        current_sum: int = 0
        min_len: int = len(nums)
        
        for right in range(len(nums)):
            current_sum += nums[right]

            current_remainder = current_sum % p
            
            needed = (current_remainder - target + p) % p
            
            if needed in seen:
                min_len = min(min_len, right - seen[needed])
            
            seen[current_remainder] = right
        
        return min_len if min_len < len(nums) else -1


def main() -> None:
    print('1590. Make Sum Divisible by P')

    sol = Solution()
    
    print(sol.minSubarray([3,1,4,2], 6))
    print(sol.minSubarray([6,3,5,2], 9))
    print(sol.minSubarray([1,2,3], 3))
    print(sol.minSubarray([7], 2))


if __name__ == '__main__':
    main()