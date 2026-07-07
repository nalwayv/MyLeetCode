from typing import List


def sumAndMultiply(n: int) -> int:
    """Break down n into new int of non-zero digits in original order and return
    and return it multiplied by sum of digits

    Args:
        n (int):

    Returns:
        non-zero digints * sum of digits
    """

    def helper(n: int, out: List[int]) -> None:
        """Helper fn to recursively break down int
        Args:
            n (int): number to break down
            out (List[int]): out perameters to store results for [non-zero digits, sum of digits]
        """
        if n == 0:
            return

        helper(n // 10, out)

        current = n % 10
        out[1] += current
        if current != 0:
            out[0] *= 10
            out[0] += current

    result: List[int] = [0, 0]
    helper(n, result)
    return result[0] * result[1]


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
