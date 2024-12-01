class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """Given an array nums containing n distinct numbers in the range [0, n],\n
        return the only number in the range that is missing from the array.

        Args:
            nums (list[int]): list of ints in range from 0-n in random order.
        Returns:
            int: 
                Missing number from range.
        """
        n: int = len(nums)
        
        # n * (n+1) / 2 = formula sum for ints in range 1-n
        total: int = (n * (n+1)) // 2

        # subtracting from total should reveal missing number
        for num in nums:
            total -= num
    
        return total
    

def case1(sol: Solution) -> None:
    nums: list[int] = [3,0,1]
    print(f"case 1: {sol.missingNumber(nums)} == 2")


def case2(sol: Solution) -> None:
    nums: list[int] = [9,6,4,2,3,5,7,0,1]
    print(f"case 2: {sol.missingNumber(nums)} == 8")


def main() -> None:
    print("268. Missing Number")
    sol = Solution()
    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()