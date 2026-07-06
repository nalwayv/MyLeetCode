from typing import List


def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    """Return how many intervals are left after remove all intervals that are covered by another.

    Args:
        intervals(List[List[int]]): list of intervals [start, end]

    Returns:
        The amount of intervals left
    """

    def is_covered(a: int, b: int, c: int, d: int) -> bool:
        """Check if interval [a, b] is covered by interval [c, d]
        Returns:
            true if [a, b] is covered by [c, d]
        """
        return c <= a and b <= d

    # sort intervals by end
    s_intervals: List[List[int]] = sorted(intervals, key=lambda interval: interval[1])

    n: int = len(s_intervals)
    count: int = n
    for i in range(n - 2, -1, -1):
        a: int = s_intervals[i][0]
        b: int = s_intervals[i][1]
        c: int = s_intervals[i + 1][0]
        d: int = s_intervals[i + 1][1]

        # if interval[i] covers interval[i+1] or interval[i+1] covers interval[i] then merge.
        if is_covered(a, b, c, d):
            s_intervals[i][0] = c
            s_intervals[i][1] = d
            count -= 1
        elif is_covered(c, d, a, b):
            s_intervals[i + 1][0] = a
            s_intervals[i + 1][1] = b
            count -= 1

    return count


def test_case(intervals: List[List[int]], expected: int) -> None:
    test: bool = removeCoveredIntervals(intervals) == expected
    result: str = "pass" if test else "fail"
    print(f"Test Result: {result}")


def main() -> None:
    print("1288. Remove Covered Intervals")

    intervals_1: List[List[int]] = [[1, 4], [3, 6], [2, 8]]
    test_case(intervals_1, 2)

    intervals_2: List[List[int]] = [[1, 4], [2, 3]]
    test_case(intervals_2, 1)

    intervals_3: List[List[int]] = [
        [1, 4],
        [3, 6],
        [2, 8],
        [1, 9],
        [1, 2],
        [3, 4],
        [5, 6],
        [3, 7],
    ]
    test_case(intervals_3, 1)

    intervals_4: List[List[int]] = [[3, 10], [4, 10], [5, 11]]
    test_case(intervals_4, 2)


if __name__ == "__main__":
    main()
