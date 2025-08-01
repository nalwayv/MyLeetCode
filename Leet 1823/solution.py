class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums: list[int] = [i+1 for i in range(n)]
        
        j: int = 0
        for _ in range(len(nums) - 1):
            j = (j + (k-1)) % len(nums)
            nums.pop(j)

        return nums[0]


def main() -> None:
    print("1823. Find the Winner of the Circular Game")

    sol = Solution()
    
    print(sol.findTheWinner(n=5, k=2))
    print(sol.findTheWinner(n=6, k=5))


if __name__ == "__main__":
    main()