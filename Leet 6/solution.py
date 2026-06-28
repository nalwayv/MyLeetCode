def solve(s: str, numRows: int) -> str:
    # store each of the parts of the string that will form the final result
    builder: list[str] = [""] * numRows
    at: int = 0
    step: int = 0

    for ch in s:
        builder[at] += ch

        # ping pong between 0 and numRows - 1 
        if at <= 0:
            step = 1
        if at >= numRows - 1:
            step = -1

        at += step

    return "".join(builder)


def main() :
    print("6. Zigzag Conversion")

    print(solve("PAYPALISHIRING", 3))
    print(solve("AB", 1))


if __name__ == "__main__":
    main()