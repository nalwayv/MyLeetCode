# Find Numbers
# Given an array nums of integers, return how many of them contain an even number of digits.

def count_digits(num: int) -> int:
    count: int = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


def is_number_of_digits_in_int_even(num: int) -> bool:
    return count_digits(num) & 1 == 0


def find_nums(nums: list[int]) -> int:
    """for each num count its digits and check if its even
    return count
    """
    count: int = 0
    for num in nums:
        if is_number_of_digits_in_int_even(num):
            count += 1

    return count


def main() -> None:
    nums: list[int] = [12, 345, 2, 6, 7896]
    result: int = find_nums(nums)
    print(result)


if __name__ == "__main__":
    main()