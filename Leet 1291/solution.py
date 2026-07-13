from typing import Final, List


def sequential_digits(low: int, high: int) -> List[int]:
    """Return a sorted list of all int in range [low, high] that have sequential digits

    Args:
        low (int): range low value
        high (int): range high value

    Returns:
        (List[int]): all numbers that have increasing digits between low and high
    """
    # NOTE:
    # Constraints:
    #   10 <= low <= high <= 10^9
    if low > high:
        raise ValueError("low must be less than or equal to high")

    digits: Final[str] = "123456789"

    result: List[int] = []

    lo: int = len(str(low))
    hi: int = len(str(high))

    for i in range(lo, hi + 1, 1):
        # window
        for k in range(0, 9 - i + 1):
            num: int = int(digits[k : k + i])
            if low <= num <= high:
                result.append(num)

    return result


def print_result(lo: int, hi: int) -> None:
    print(f"Result [{lo}, {hi}]: [", end="")
    for num in sequential_digits(lo, hi):
        print(f" {num} ", end="")
    print("]")


def main() -> None:
    print("1291. Sequential Digits")

    print_result(100, 300)
    print_result(1000, 13000)


if __name__ == "__main__":
    main()
