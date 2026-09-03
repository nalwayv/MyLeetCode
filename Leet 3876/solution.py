def uniform_array(nums1: list[int]) -> bool:
    min_odd: int = -1
    for n in nums1:
        if n % 2 == 1:
            if min_odd == -1 or n < min_odd:
                min_odd = n

    # even - odd = odd
    # that odd should be >= 1
    for n in nums1:
        if n % 2 == 0 and n - min_odd < 1:
            return False
            
    return True


def main() -> None:
    print("3876. Construct Uniform Parity Array II")

    result: str = "pass" if uniform_array([1,4,7]) else "fail"
    print(f"[1,4,7] should equal true ? {result}")


if __name__ == "__main__":
    main()
