import heapq


def shortestPath(n: int, edges: list[list[int]], labels: str, k: int) -> int:
    """
    Args:
    n (int): number of nodes
    edges (list[list[int]]): [u,v,w] - node start node end and edge weight.
    labels str: labels for each node
    k int: frequency that each label much be under onlone a path

    Returns:
        (int): shortest path with at most k consecutive identical characters
    """
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for source, destination, weight in edges:
        graph[source].append((destination, weight))

    print(graph)

    heap: list[tuple[int, int, int]] = [(0, 0, 1)]
    done_k: list[int] = [k + 1] * n

    while heap:
        current_weight, current_node, current_k = heapq.heappop(heap)
        if current_k >= done_k[current_node]:
            continue

        done_k[current_node] = current_k

        if current_node == n - 1:
            return current_weight

        for neighbour_node, neighbour_weight in graph[current_node]:
            next_k: int = (
                current_k + 1 if labels[current_node] == labels[neighbour_node] else 1
            )
            if next_k < done_k[neighbour_node]:
                heapq.heappush(
                    heap, (current_weight + neighbour_weight, neighbour_node, next_k)
                )

    return -1


def main() -> None:
    print("3970. Shortest Path With At Most K Consecutive Identical Characters")

    result_1: int = shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1)
    print("Result:", result_1)

    result_2: int = shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2)
    print("Result:", result_2)

    result_3: int = shortestPath(3, [[0, 1, 1], [1, 2, 1]], "aaa", 2)
    print("Result:", result_3)


if __name__ == "__main__":
    main()
