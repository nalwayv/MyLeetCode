class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n: int = len(nums) // 2
        table: dict[int, int] = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1
            if table[num] == n:
                return num
        return 0
    

def main() -> None:
    print('961. N-Repeated Element in Size 2N Array')

    solution = Solution()
    
    print(solution.repeatedNTimes([1,2,3,3]))
    print(solution.repeatedNTimes([2,1,2,5,3,2]))
    print(solution.repeatedNTimes([5,1,5,2,5,3,5,4]))


if __name__ == '__main__':
    main()