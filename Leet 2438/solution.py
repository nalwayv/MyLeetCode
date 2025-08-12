class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        pows: list[int] = []
        for i in range(n.bit_length()):
            if (n >> i) & 1:
                pows.append(1 << i)

        # help with product being very large
        overflow: int = int(1e9+7)

        products: list[int] = []
        for left, right in queries:
            product: int = 1
            for val in pows[left:right+1]:
                product *= val
            products.append(product % overflow)

        return products
    

def main() -> None:
    print("2438. Range Product Queries of Powers")

    sol = Solution()

    case_1: list[int] = sol.productQueries(n=15, queries=[[0, 1], [2, 2], [0, 3]])
    print(f"case 1: {case_1}")

    case_2: list[int] = sol.productQueries(n=2, queries=[[0, 0]])
    print(f"case 2: {case_2}")


if __name__ == "__main__":
    main()
