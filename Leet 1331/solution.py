from typing import Dict, List


def array_rank_transform(arr: List[int]) -> List[int]:
    """Given an array of integers arr, replace each element with its rank

    Args:
        arr (List[int]): Input array

    Returns:
        List[int]: Array with each element replaced by its rank
    """
    if not arr:
        return []

    sorted_arr: List[int] = sorted(arr)

    # update ranking
    ranking: Dict[int, int] = {sorted_arr[0]: 1}
    rank: int = 1

    for i in range(1, len(arr)):
        curr: int = sorted_arr[i]
        prev: int = sorted_arr[i - 1]

        if curr == prev:
            ranking[curr] = rank
        else:
            rank += 1
            ranking[curr] = rank

    result: List[int] = [0] * len(arr)
    for idx, val in enumerate(arr):
        result[idx] = ranking[val]

    return result


def test_case(arr: List[int], expected: List[int]):
    result: List[int] = array_rank_transform(arr)

    if len(result) != len(expected):
        print("Result: Not the same length fail")
        return

    for a, b in zip(result, expected):
        if a != b:
            print("Result: result does not match expected fail")
            return

    print("Result: pass")


def main() -> None:
    print("1331. Rank Transform of an Array")

    arr_1: List[int] = [40, 10, 20, 30]
    expected_1: List[int] = [4, 1, 2, 3]
    test_case(arr_1, expected_1)

    arr_2: List[int] = [100, 100, 100]
    expected_2: List[int] = [1, 1, 1]
    test_case(arr_2, expected_2)

    arr_3: List[int] = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    expected_3: List[int] = [5, 3, 4, 2, 8, 6, 7, 1, 3]
    test_case(arr_3, expected_3)


if __name__ == "__main__":
    main()
