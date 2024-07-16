# Squares of a Sorted array
#
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.
#

# HELPERS

def sqr(num: int) -> int:
    return num * num


def bleft(nums: list[int], value: int, lo: int, hi: int) -> int:
    if lo < 0:
        return -1
    
    if lo > hi:
        return -1
    
    while lo < hi:
        mid: int = (lo + hi) // 2

        if nums[mid] < value:
            lo = mid + 1

        else:
            hi = mid

    return lo


# USING SORT


def sorted_squares(nums: list[int]) -> list[int]:
    """mine using sort"""
    n: int = len(nums)
    result: list[int] = [0] * 5

    for i in range(n):
        result[i] = sqr(nums[i])
        
    result.sort()

    return result


# USING ABS


def sorted_squares_b(nums: list[int]) -> list[int]:
    """leet version that uses abs to check"""
    n: int = len(nums)
    result: list[int] = [0] * 5

    start: int = 0
    end: int = n - 1
    p1: int = end

    while start < end:
        if abs(nums[start]) > abs(nums[end]):
            result[p1] = sqr(nums[start])
            start += 1

        else:
            result[p1] = sqr(nums[end])
            end -= 1

        p1 -= 1

    return result


# USING BISECT LEFT


def sorted_squares_c(nums: list[int]) -> list[int]:
    """using bisect_left to find coord to place value at
    """
    n: int = len(nums)

    result: list[int] = []

    for i in range(n):
        value: int = sqr(nums[i])

        if result:
            at: int = bleft(result, value, 0, i)

            if at != -1:
                result.insert(at, value)
        
        else:
            result.append(value)

    return result


# MAIN


def main() -> None:
    nums: list[int] = [-4, -1, 0, 3, 10]
    result: list[int] = sorted_squares_c(nums)
    print(result)


if __name__ == "__main__":
    main()
