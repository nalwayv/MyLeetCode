class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Counts the number of good pairs in the given list of integers.
        A pair (i, j) is called good if nums[i] == nums[j] and i < j.
        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The number of good pairs in the list.
        """
        count: int = 0 
        table: dict[int, int] = {}

        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                count += table[num]
                table[num] += 1

        return count


def main() -> None:
    print("1512. Number of Good Pairs")

    sol = Solution()
    nums = [1,2,3,1,1,3]
    print(sol.numIdenticalPairs(nums))


if __name__ == "__main__":
    main()
        