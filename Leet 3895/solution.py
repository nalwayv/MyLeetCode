def count_digit_occurrences(nums: list[int], digit: int) -> int:
    """Return the sum of counting the occurence of digit within each number within nums.

    Args:
        nums (list[int]): list of ints.
        digit: single digit to search for within each number.

    Returns:
        int: topal occurences of digit within each of the numbers within nums.

    Raises:
        ValueError: if digit is < 0 or > 9
    """
    if digit < 0 or digit > 9:
        raise ValueError("digit must be a single digit (0-9)")

    str_digit: str = str(digit)

    count: int = 0
    for num in nums:
        for value in str(num):
            if value == str_digit:
                count += 1

    return count


def main() -> None:
    print("3895. Count Digit Appearances")

    count: int = count_digit_occurrences([12,54,32,22], 2)
    result: str = "pass" if count == 4 else "fail"
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
