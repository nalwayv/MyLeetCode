from collections import deque
from sys import maxsize
from typing import Deque, Dict, List, Set


def minScore(roads: List[List[int]]) -> int:
    """
    Given a bidirectional graph with cities from 1 to n and roads with distanceces
    between each connected city,
    return the minumum possible score of a path between 1 and n.

    Args:
        roads (List[List[int]]): graph with cities labeled from 1 to n and roads with distance costs.

    Returns:
        int: min cost of one of the possible roads taken from 1 to n
    """
    # build bidirectional graph
    graph: Dict[int, Dict[int, int]] = {}
    # assuming that each value in roads is of length 3 [start, end, edge]
    for start, end, edge in roads:
        if start not in graph:
            graph[start] = {}

        if end not in graph:
            graph[end] = {}

        graph[start][end] = edge
        graph[end][start] = edge

    # get min score
    que: Deque[int] = deque([1])
    visited: Set[int] = {1}
    result: int = maxsize

    while que:
        curr: int = que.popleft()

        for key, val in graph[curr].items():
            result = min(result, val)

            if key not in visited:
                visited.add(key)
                que.append(key)

    return result


def main() -> None:
    print("2492. Minimum Score of a Path Between Two Cities")

    roads: List[List[int]] = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]
    score: int = minScore(roads)
    print(f"Min Score: {score}")


if __name__ == "__main__":
    main()
