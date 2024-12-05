class Solution:
    """
    Given an array arr of integers, check if there exist two indices i and j such that

    i != j,
    0 <= i,
    j < len( arr ),
    arr[ i ] == 2 * arr[ j ]

    Args:
        arr (list[int]): check if doubles of current exist

    Returns:
        found a double that exists of current value at different location
    """
    def check_if_exist(self, arr: list[int]) -> bool:
        # use values as keys
        data: dict[int, int] = {}
        for i, num in enumerate(arr):
            data[num] = i

        for j, num in enumerate(arr):
            # does data contain a double of current
            db: int = num * 2
            if db in data:
                # check i != j
                if data[db] != j:
                    return True

        return False


def main() -> None:
    print("1346. Check If N and Its Double Exist")

    sol = Solution()

    case1: list[int] = [10,2,5,3]
    result1 = "pass" if sol.check_if_exist(case1) else "fail"
    print(f"Case1: {result1}")

    case2: list[int] = [3,1,7,11]
    result2 = "pass" if not sol.check_if_exist(case2) else "fail"
    print(f"Case2: {result2}")


if __name__ == "__main__":
    main()