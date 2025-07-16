class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        """Given an integer array nums, in which exactly two elements appear only once
        and all the other elements appear exactly twice. 
        Find the two elements that appear only once. You can return the answer in any order.

        Args:
            nums (list[int]): list of elements with exactly two elements appearing only once.

        Returns:
            list[int]: single numbers from nums.
        """
        table: dict[int, int] = {}
        numbers: set[int] = set(nums)
        duplicate: set[int] = set()

        for num in nums:
            table[num] = table.get(num, 0) + 1
            if table[num] > 1:
                duplicate.add(num)
        
        return [num for num in numbers ^ duplicate]


def main() -> None:
    print("260. Single Number III")

    sol = Solution()

    print("case 1")
    print(sol.singleNumber(nums= [1,2,1,3,2,5]))

    print("case 2")
    print(sol.singleNumber(nums= [-1, 0]))

    print("case 3")
    print(sol.singleNumber(nums= [0, 1]))


if __name__ == "__main__":
    main()