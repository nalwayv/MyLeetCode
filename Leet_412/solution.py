# FIZZ BUZZ
#
# FIZZ if n is devisable by 3
# BUZZ if n is devisable by 5
# FIZZBUZZ if n is devisable by 3 and 5


def fizzBuzz(n: int) -> list[str]:
    """FizzBuzz
    """
    FIZZ: str = "Fizz"
    BUZZ: str = "Buzz"

    result: list[str] = []

    for i in range(1, n + 1):
        data: list[str] = []

        if i % 3 == 0:
            data.append(FIZZ)
        
        if i % 5 == 0:
            data.append(BUZZ)

        if not data:
            data.append(str(i))
        
        result.append("".join(data))

    return result


def fizzBuzz2(n: int) -> list[str]:
    FIZZ: str = "Fizz"
    BUZZ: str = "Buzz"
    FIZZBUZZ: str = "FizzBuzz"

    result: list[str] = []

    for i in range(1, n + 1):
        d3: bool = i % 3 == 0
        d5: bool = i % 5 == 0

        if d3 and d5:
            result.append(FIZZBUZZ)
        elif d3:        
            result.append(FIZZ)
        elif d5:
            result.append(BUZZ)
        else:
            result.append(str(i))

    return result


def main() -> None:
    print(fizzBuzz(15))
    print(fizzBuzz2(15))


if __name__ == "__main__":
    main()