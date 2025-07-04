class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set: set[int] = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False


def main() -> None:
    solution = Solution()
    nums: list[int] = [1,1,1,3,3,4,3,2,4,2]
    print(f"Input: nums = {nums}")
    print(f"Output: {solution.containsDuplicate(nums)}")


if __name__ == "__main__":
    main()
    