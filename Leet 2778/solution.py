def sum_of_squares(nums: list[int]) -> int:
    """Return the sum of the squares of all special elements of nums.

    Args:
        nums (list[int]): list of positive non zero int values.

    Returns:
        int: square sum of special elements from nums
    """
    n: int = len(nums)
    result: int = 0
    for i, num in enumerate(nums, start=1):
        if n % i == 0:
            result += (num * num)
    return result


def main() -> None:
    print("2778. Sum of Squares of Special Elements")

    result: str = "pass" if sum_of_squares([1,2,3,4]) == 21 else "fail"
    print(f"Result for sum_of_squared([1,2,3,4]) should equal 21? {result}")


if __name__ == "__main__":
    main()
