def uniformArray(nums1: list[int]) -> bool:
    # all even = true
    # all odd = true
    # As long as there is at least one odd number in the array, you can always flip all even numbers into odd 
    #  odd - even = odd
    #  even - odd = odd

    # return True

    odds = sum(1 for x in nums1 if x %2==1)
    return odds == 0 or odds >= 1


def main() -> None:
    print("3875. Construct Uniform Parity Array I")

    print(uniformArray([5,3,1,2,4]))
    print(uniformArray([2,4,6,8]))


if __name__ == "__main__":
    main()