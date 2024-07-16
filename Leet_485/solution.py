# Max Consecutive Ones
#
# Given a binary array nums, return the maximum number 
# of consecutive 1's in the array.
#

def max_ones(nums: list[int]) -> int:
    """return max ones in a row
    
    example 1
    
    max_ones([1, 0, 1, 1, 0]) = 2
             |+| - |+  +| -   = 2
    """
    max_count: int = 0

    p1: int = 0
    p2: int = 0
    end: int = len(nums)

    while p1 < end:
        p2 = p1

        count: int = 0
        while p2 < end and nums[p2] == 1:
            count += 1
            p2 += 1
        
        max_count = max(max_count, count)
    
        p1 = p2 + 1

    return max_count


# def max_ones_other(nums: list[int]) -> int:
#     h: int = 0
#     c: int = 0

#     for num in nums:
#         if num == 1:
#             c += 1
#         else:
#             h = max(h, c)
#             c = 0

#     h = max(h, c)

#     return h


def main() -> None:
    data: list[int] = [1,1,0,1,1,1]
    result:int = max_ones(data)
    print(result)


if __name__ == "__main__":
    main()