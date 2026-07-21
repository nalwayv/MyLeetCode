def max_active_sections_after_trade(s: str) -> int:
    """
    Args:
        s (str): A string made up of 0 and 1

    Returns:
        int
    """
    one: int = 0
    zero: int = 0
    max_trade: int = 0

    n: int = len(s)
    i: int = 0
    while i < n:
        # get len of block of same type
        j: int = i
        while j < n and s[i] == s[j]:
            j += 1

        diff: int = j - i
        if s[i] == "1":
            one += diff
        else:
            if zero > 0:
                max_trade = max(max_trade, diff + zero)
            zero = diff

        i = j

    return max_trade + one


def main() -> None:
    print("3499. Maximize Active Section with Trade I")

    print("Result: 1 ==", max_active_sections_after_trade("01"))
    print("Result: 4 ==", max_active_sections_after_trade("0100"))
    print("Result: 7 ==", max_active_sections_after_trade("1000100"))
    print("Result: 4 ==", max_active_sections_after_trade("01010"))
    print("Result: 11 ==", max_active_sections_after_trade("01010101010101101"))


if __name__ == "__main__":
    main()
        