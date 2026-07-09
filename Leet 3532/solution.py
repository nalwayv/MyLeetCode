from typing import List


def pathExistenceQueries(
    n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
) -> List[bool]:
    """
    Args:
        n int: range of nodes
        nums (List[int]): edge costs
        maxDiff int: max diff allowed between two nodes
        queries (List[List[int]]): queries if path exists

    Returns:
        List[bool]: list of true or false values if path exists
    """
    # Group nodes by connected components based on maxDiff
    nodes: List[int] = [0] * n
    count: int = 0
    for i in range(1, n):
        if abs(nums[i] - nums[i - 1]) > maxDiff:
            count += 1
        nodes[i] = count

    # Check each query for path existence
    result: List[bool] = []
    for start, end in queries:
        result.append(nodes[start] == nodes[end])
    return result


def test_case(maxdiff: int, nums: List[int], queries: List[List[int]]) -> None:
    result: List[bool] = pathExistenceQueries(len(nums), nums, maxdiff, queries)
    print("Result= [", end="")
    for value in result:
        print(f" {value} ", end="")
    print("]")


def main() -> None:
    print("3532. Path Existence Queries in a Graph I")

    nums1: List[int] = [1, 3]
    queries1: List[List[int]] = [[0, 0], [0, 1]]
    test_case(1, nums1, queries1)

    nums2: List[int] = [2, 5, 6, 8]
    queries2: List[List[int]] = [[0, 1], [0, 2], [1, 3], [2, 3]]
    test_case(2, nums2, queries2)

    nums3: List[int] = [2975, 50642]
    queries3: List[List[int]] = [[1, 0]]
    test_case(6, nums3, queries3)


if __name__ == "__main__":
    main()
