class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Given a non-negative integer num, returns the maximum valued number you can get by swapping two digits at most once.
        Args:
            num (int): The input non-negative integer.
        Returns:
            int: The maximum number obtainable by swapping two digits at most once.
        Example:
            maximumSwap(2736) -> 7236
            maximumSwap(9973) -> 9973
        """
        max_num: int = num

        nums: list[str] = []
        while num:
            nums.insert(0, str(num % 10))
            num //= 10

        n: int = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                # swap
                nums[i], nums[j] = nums[j], nums[i]

                max_num = max(max_num, int("".join(nums)))
                
                # reset swap
                nums[i], nums[j] = nums[j], nums[i]

        return max_num
    

def main() -> None:
    print("670. Maximum Swap")

    sol = Solution()
    
    print(sol.maximumSwap(2736))
    print(sol.maximumSwap(9973))


if __name__ == "__main__":
    main()