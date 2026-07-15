import math


def gcd_of_odd_even_sums(n: int) -> int:
    even: int = 1
    odd: int = 2
    even_sum: int = 0
    odd_sum: int = 0

    for _ in range(n):
        even_sum += even
        even += 2

        odd_sum += odd
        odd += 2

    return math.gcd(even_sum, odd_sum)


def main() -> None:
    print("3658. GCD of Odd and Even Sums")
    print(f"Result n=4: {gcd_of_odd_even_sums(4)}")
    print(f"Result n=5: {gcd_of_odd_even_sums(5)}")


if __name__ == "__main__":
    main()
