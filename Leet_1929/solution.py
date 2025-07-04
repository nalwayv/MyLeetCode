class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        n2: int = n * 2
        return [nums[i%n] for i in range(n2)]
    

def main() -> None:
    print("1929. Concatenation of Array")

    sol = Solution()
    
    print(sol.getConcatenation([1,2,1]))
    print(sol.getConcatenation([1,2,3,4,5,6,7,8,9]))


if __name__ == "__main__":
    main()