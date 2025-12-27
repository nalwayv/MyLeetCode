class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen: set[int] = set()
        duplicate_number: int = 0
        for num in nums:
            if num in seen:
                duplicate_number = num
            seen.add(num)

        for i in range(len(nums)):
            if i+1 not in seen:
                return [duplicate_number, i+1]
            
        return []


def main() -> None:
    print('645. Set Mismatch')

    sol = Solution()
    
    print(sol.findErrorNums([1,2,2,4]))
    print(sol.findErrorNums([1,1]))
    print(sol.findErrorNums([1,3,4,4,2]))
    print(sol.findErrorNums([2,2]))
    print(sol.findErrorNums([3,2,3,4,6,5]))


if __name__ == '__main__':
    main()