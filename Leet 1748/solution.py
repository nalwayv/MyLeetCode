class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        table:dict[int, int] = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1

        result: int = 0
        for k, v in table.items():
            if v == 1:
                result += k

        return result


def main() -> None:
    print("1748. Sum of Unique Elements")

    sol = Solution()
    
    print(sol.sumOfUnique([1,2,3,2]))           # 4
    print(sol.sumOfUnique([1,1,1,1,1]))         # 0
    print(sol.sumOfUnique([1,2,3,4,5]))         # 15
    print(sol.sumOfUnique([10,6,9,6,9,6,8,7]))  # 25


if __name__ == "__main__":
    main()