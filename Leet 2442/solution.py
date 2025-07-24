class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        distinct: set[int] = set(nums)
        
        for num in nums:
            if num > 9: 
                reversed_num: int = 0
                while num:
                    reversed_num *= 10
                    reversed_num += num % 10
                    num //= 10

                distinct.add(reversed_num)
            else:
                distinct.add(num)

        return len(distinct)


def main() -> None:
    print("2442. Count Number of Distinct Integers After Reverse Operations")

    sol = Solution()
    
    print(sol.countDistinctIntegers(nums=[1,13,10,12,31]))
    print(sol.countDistinctIntegers(nums=[2,2,2]))


if __name__ == "__main__":
    main()