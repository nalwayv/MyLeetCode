from typing import NamedTuple


class Span(NamedTuple):
    price: int
    span: int


class StockSpanner:
    def __init__(self):
        self.stack: list[Span] = []

    def next(self, price: int) -> int:
        span: int = 1
        while self.stack and self.stack[-1].price <= price:
            span += self.stack.pop().span

        self.stack.append(Span(price, span))

        return span


def main() -> None:
    print("901. Online Stock Span")

    stock = StockSpanner()

    print(stock.next(100)) # return 1
    print(stock.next(80))  # return 1
    print(stock.next(60))  # return 1
    print(stock.next(70))  # return 2
    print(stock.next(60))  # return 1
    print(stock.next(75))  # return 4
    print(stock.next(85))  # return 6


if __name__ == "__main__":
    main()