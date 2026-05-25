import functools

class Solution:
    def canJump(self, nums: list[int]) -> bool:

        @functools.cache
        def jump_to(i: int = 0) -> bool:
            if i >= len(nums) - 1:
                return True

            amount = i + nums[i]
            if amount > len(nums) - 1:
                amount = len(nums) - 1
             
            for j in range(i + 1, amount + 1):
                if jump_to(j):
                    return True
                
            return False
    
        return jump_to()
    

def main() -> None:
    print("55. Jump Game")
    print(Solution().canJump([2,3,1,1,4]))


if __name__ == "__main__":
    main()