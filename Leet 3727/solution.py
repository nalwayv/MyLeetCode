def maxAlternatingSum(nums: list[int]) -> int:
    cpy: list[int] = [abs(i) for i in nums]
    cpy.sort()

    n: int = len(cpy)

    result: int = 0
    for i in range(n // 2):
        end: int = cpy[n - i - 1]
        start: int = cpy[i]

        result += end * end
        result -= start * start

    if n % 2 == 1:
        mid: int = cpy[n // 2]
        result += mid * mid

    return result
