def maxAlternatingSum(nums: list[int]) -> int:
    cpy: list[int] = [abs(i) for i in nums]
    cpy.sort()

    n: int = len(cpy)

    result: int = 0
    for lo in range(n // 2):
        hi: int = n - lo - 1

        result += cpy[hi] * cpy[hi]
        result -= cpy[lo] * cpy[lo]

    if n % 2 == 1:
        mid: int = n // 2
        result += cpy[mid] * cpy[mid]

    return result
