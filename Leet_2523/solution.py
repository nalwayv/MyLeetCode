class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        # get primes
        n: int = right + 1
        primes: list[bool] = [True] * n
        primes[0] = False
        primes[1] = False
        for i in range(2, n):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False

        # get primes in range needed
        numbers: list[int] = []
        for i in range(left, right + 1):
            if primes[i]:
                numbers.append(i)

        
        result: list[int] = [-1, -1]
        min_diff: float = float("inf")
        for i in range(1, len(numbers)):
            diff: int = numbers[i] - numbers[i-1]
            if diff < min_diff:
                min_diff = diff

                result[0] = numbers[i-1]
                result[1] = numbers[i]

        return result


#-----------------------------------------------------------------------
# MAIN


def main() -> None:
    print("2523. Closest Prime Numbers in Range")

    sol = Solution()

    print(f"{sol.closestPrimes(10, 19)} == [11, 13]")
    print(f"{sol.closestPrimes(4, 6)} == [-1, -1]")


if __name__ == "__main__":
    main()