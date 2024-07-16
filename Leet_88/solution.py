# Merge sorted arrays
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# Example 1:
#
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
# Example 2:
#
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
#
# Example 3:
#
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# def merge_b(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     """pythonic"""
#     if m + n != len(nums1):
#         return

#     if n <= 0:
#         return 

#     arr: list[int] = sorted(nums1[0 : m] + nums2)

#     for i, _ in enumerate(nums1):
#         nums1[i] = arr[i]


# 
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    lo: int = 0
    hi: int = m + n
    mid: int = m

    p1: int = 0
    p2: int = mid

    # concat nums1 and nums2
    arr: list[int] = nums1[0 : m] + nums2

    # add back to nums1 in sorted order
    for p3 in range(lo, hi):
        # use values nums1 if
        #   p1 in range and
        #   p2 out of range or value at p1 less then or equil to value at p2
        # else use values in nums2
        if p1 < mid and (p2 >= hi or arr[p1] <= arr[p2]):
            nums1[p3] = arr[p1]
            p1 += 1
        else:
            nums1[p3] = arr[p2]
            p2 += 1


# TEST CASES


def case_1() -> None:
    print("CASE 1")
    nums1: list[int] = [1, 2, 3, 0, 0, 0]
    m: int = 3
    
    nums2: list[int] = [2, 5, 6]
    n: int = 3

    merge(nums1, m, nums2, n)
    print(nums1)


def case_2() -> None:
    print("CASE 2")
    
    nums1: list[int] = [1]
    m: int = 1
    
    nums2: list[int] = [0]
    n: int = 0

    merge(nums1, m, nums2, n)
    print(nums1)


def case_3() -> None:
    print("CASE 3")

    nums1: list[int] = [0]
    m: int = 0
    
    nums2: list[int] = [1]
    n: int = 1

    merge(nums1, m, nums2, n)
    print(nums1)


def main() -> None:
    case_1()
    case_2()
    case_3()


if __name__ == "__main__":
    main()