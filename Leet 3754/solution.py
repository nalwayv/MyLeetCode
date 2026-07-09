from typing import Tuple


def sumAndMultiply(n: int) -> int:
    """Rebuild n from its non-zero digits (in original order) and multiply
    that number by the sum of all its digits

    Args:
        n (int): non negative number

    Returns:
        (non zero digits) * (sum of digits)

    Raises:
        ValueError if n < 0
    """
    if n < 0:
        raise ValueError("n must be non negative")

    def helper(n: int) -> Tuple[int, int]:
        """Helper fn to recursively break down int then rebuild into digits and sum of digits for out parameter

        Args:
            n (int): number to break down
            args (Dict[str, int]): dict that contains kwargs 'non_zero_digits' and 'sum_of_digits' to store result from breaking down n
        """
        if n == 0:
            return (0, 0)

        # break down int
        non_zero_digits, sum_of_digits = helper(n // 10)

        digit: int = n % 10
        sum_of_digits += digit
        if digit != 0:
            non_zero_digits *= 10
            non_zero_digits += digit
        return (non_zero_digits, sum_of_digits)

    non_zero_digits, sum_of_digits = helper(n)

    return non_zero_digits * sum_of_digits


def test_case(n: int, expected: int) -> None:
    result: str = "pass" if sumAndMultiply(n) == expected else "fail"
    print(f"Test Case {n} equals {expected} ? {result}")


def main() -> None:
    print("3754. Concatenate Non-Zero Digits and Multiply by Sum I")

    # 1234 * 10
    test_case(10203004, 12340)
    # 55555 * 25
    test_case(505050505, 1388875)


if __name__ == "__main__":
    main()
