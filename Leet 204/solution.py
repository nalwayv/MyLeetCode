class Solution:
    def countPrimes(self, n: int) -> int:
        """Count prines using `Sieve of Eratosthenes` method
        """
        if n <= 1:
            return 0
        
        arr: list[bool] = [True for _ in range(n)]
        arr[0] = False
        arr[1] = False

        for i in range(2, n):
            if arr[i]:
                for j in range(i*i, n, i):
                    arr[j] = False

        return arr.count(True)


def main() -> None:
    print("204. Count Primes")

    sol = Solution()
    
    print(f"= {sol.countPrimes(10)}")
    print(f"= {sol.countPrimes(0)}")
    print(f"= {sol.countPrimes(1)}")
    print(f"= {sol.countPrimes(5000000)}")


if __name__ == "__main__":
    main()