# Number of Steps to Reduce a Number to Zero
#
# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, 
# otherwise, you have to subtract 1 from it.


def numberOfSteps(num: int) -> int:
    result: int = 0
    
    while num > 0:
        # bitwise is even

        if (num ^ 1) == (num + 1):
            num //= 2
        else:
            num -= 1

        result += 1

        # # full bitwise
        # if (num & 1) == 0:
        #     num >>= 1
        # else:
        #     num -= 1
        # result += 1

    return result


def main() -> None:
    cases: list[tuple[int, int]] = [
        (14, 6),
        (8, 4),
        (123, 12)
    ]

    for case in cases:
        number, result = case
        print(numberOfSteps(number) == result)

if __name__ == "__main__":
    main()
