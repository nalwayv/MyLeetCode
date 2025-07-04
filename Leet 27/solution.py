# Remove Element

def remove_element(nums: list[int], val: int) -> int:
    # remove from nums all elements that equal val
    n: int = len(nums)
    if n == 1 and nums[0] == val:
        return 0

    k: int = n
    for i in reversed(range(n)):
        if nums[i] == val:
            nums[i], nums[k - 1] = nums[k - 1], nums[i]
            k -= 1

    return k


def case_1() -> None:
    print("CASE 1")

    nums: list[int] = [0,1,2,2,3,0,4,2]
    val: int = 2
    print(f"Remove {val} from {nums}")
    print(f"RESULT: {remove_element(nums, val)}, NUMS: {nums}")
    print("-" * 10)


def case_2() -> None:
    print("CASE 2")

    nums: list[int] = [3,2,2,3]
    val: int = 3

    print(f"Remove {val} from  {nums}")
    print(f"RESULT: {remove_element(nums, val)}, NUMS: {nums}")
    print("-" * 10)


def case_3() -> None:
    print("CASE 3")

    nums: list[int] = [2]
    val: int = 2

    print(f"Remove {val} from  {nums}")
    print(f"RESULT: {remove_element(nums, val)}, NUMS: {nums}")
    print("-" * 10)


def main() -> None:
    case_1()
    case_2()
    case_3()


if __name__ == "__main__":
    main()