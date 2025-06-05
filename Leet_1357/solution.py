class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.nth: int = n
        self.discount: float = (100 - discount) / 100
        self.count: int = 0
        self.table: dict[int, int] = {a:b for a,b in zip(products, prices)}

    def getBill(self, product: list[int], amount: list[int]) -> float:
        """
        Calculates the total bill for the given products and their quantities, applying a discount every nth call.
        
        Args:
            product (list[int]): List of product IDs to be purchased.
            amount (list[int]): List of quantities corresponding to each product ID.
        
        Returns:
            float: The total bill amount after applying the discount if applicable.
        """
        self.count += 1

        apply_discount: bool = False
        if self.count == self.nth:
            apply_discount = True
            self.count = 0

        total: float = 0.0
        for a, b in zip(product, amount):
            if a in self.table:
                total += (self.table[a] * b)

        if apply_discount:
            return total * self.discount
        return total


def main() -> None:
    print("1357. Apply Discount Every n Orders")

    cashier = Cashier(3, 50, [1,2,3,4,5,6,7], [100,200,300,400,300,200,100])

    print(cashier.getBill([1,2],[1,2]))
    print(cashier.getBill([3,7],[10,10]))
    print(cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]))
    print(cashier.getBill([4],[10]))
    print(cashier.getBill([7,3],[10,10]))
    print(cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]))
    print(cashier.getBill([2,3,5],[5,3,2]))


if __name__ == "__main__":
    main()