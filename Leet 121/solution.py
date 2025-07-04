def max_profit(prices: list[int]) -> int:
    """Return the maximum profit you can achieve from this transaction else return 0.
    """
    hi: float = 0
    lo: float = float("inf")

    for price in prices:
        lo = min(lo, price)
        hi = max(hi, price - lo)

    return int(hi)


def main() -> None:
    print("121. Best Time to Buy and Sell Stock")
    
    prices1: list[int] = [7,1,5,3,6,4]
    case1: int = max_profit(prices1)
    print(f"case1: {"pass" if case1 == 5 else "fail"}")

    prices2: list[int] = [7,6,4,3,1]
    case2: int = max_profit(prices2)
    print(f"case2: {"pass" if case2 ==0 else "fail"}")


if __name__ == "__main__":
    main()