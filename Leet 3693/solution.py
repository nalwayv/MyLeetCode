from sys import maxsize


def climbStairs(n: int, costs: list[int]) -> int:
    a: int = maxsize - 9
    b: int = maxsize - 4
    c: int = 0
    for i in range(n):
        curr: int = costs[i] + min(a + 9, b + 4, c + 1)
        a = b
        b = c
        c = curr
    return c


def main() -> None:
    print("3693. Climbing Stairs II")
    result: int = climbStairs(n=4, costs=[1, 2, 3, 4])
    print(f"Result for costs=[1,2,3,4] is {result}")


if __name__ == "__main__":
    main()
