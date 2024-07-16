# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# Example
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def remove_duplicates(nums: list[int]) -> int:
    """nums has to be sorted
    """
    n: int = len(nums)
    p1: int = 0
    k: int = 0

    while p1 < n:

        p2: int = p1

        while p2 < n - 1 and nums[p2] == nums[p2 + 1]:
            p2 += 1

        nums[k] = nums[p1]

        k += 1
        p1 = p2 + 1

    return k


def remove_duplicates_2(nums: list[int]) -> int:
    """
    leet code
    """
    w: int = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[w] = nums[r]
            w += 1

    return w


def case_1() -> None:
    print("CASE 1")
    nums: list[int] = [1, 1, 2]
    print(f"Input: nums = {nums}")
    result: int = remove_duplicates_2(nums)
    print(f"Output: {result}, nums = {nums[0:result]}")
    print("-" * 10)


def case_2() -> None:
    print("CASE 2")
    nums: list[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"Input: nums = {nums}")
    result: int = remove_duplicates_2(nums)
    print(f"Output: {result}, nums = {nums[0:result]}")
    print("-" * 10)


def main() -> None:
    case_1()
    case_2()


if __name__ == "__main__":
    main()