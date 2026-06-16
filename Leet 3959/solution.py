def checkGoodInteger(n: int) -> bool:
    dsum: int = 0
    ssum: int = 0
    
    while n > 0:
        current: int = n % 10

        dsum += current
        ssum += (current * current)
        
        n //=10

    return (ssum - dsum) >= 50


def main() -> None:
    print("3959. Check Good Integer")

    print(f"is 19 a good int? {checkGoodInteger(19)}")
    print(f"is 100 a good int? {checkGoodInteger(100)}")


if __name__ == "__main__":
    main()