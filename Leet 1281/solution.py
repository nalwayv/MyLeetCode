class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n == 0:
            return 0
        
        product_n: int = 1
        sum_n: int = 0

        while n > 0:
            v: int = n % 10
            product_n *= v
            sum_n += v
            n //= 10
        
        return product_n - sum_n


def main() -> None:
    print("1281. Subtract the Product and Sum of Digits of an Integer")

    sol = Solution()
    
    print(sol.subtractProductAndSum(234))
    print(sol.subtractProductAndSum(4421))


if __name__ == "__main__":
    main()