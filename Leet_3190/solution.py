# You are given an integer array nums. In one operation, 
# you can add or subtract 1 from any element of nums.
# Return the minimum number of operations to make all elements 
# of nums divisible by 3.

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count: int = 0
        for num in nums:
            for i in [-1, 1]:
                if (num + i) % 3 == 0:
                    count += 1
        return count
    

def main() -> None:
    print("3190. Find Minimum Operations to Make All Elements Divisible by Three")
    
    sol = Solution()

    print(sol.minimumOperations([1,2,3,4]))
    print(sol.minimumOperations([3,6,9]))


if __name__ == "__main__":
    main()
        