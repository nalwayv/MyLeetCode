from typing import List


def count_complete_components(n: int, edges: List[List[int]]) -> int:
    """Return the number of complete connected components of the graph

    Note:
        a complete connected component has all nodes connected to all other nodes

    Args:
        n (int): number of nodes 0 - n-1
        edges (List[List[int]]): describe how graph nodes are connected

    Returns:
        number of connected components
    """
    # graph of nodes 0-n-1 with nodes they are connected to
    graph: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited: List[bool] = [False] * n
    result: int = 0

    for i in range(n):
        if visited[i]:
            continue

        # dfs
        stk: List[int] = [i]
        node_count: int = 0
        edge_count: int = 0

        while stk:
            current: int = stk.pop()

            if visited[current]:
                continue

            visited[current] = True

            node_count += 1
            edge_count += len(graph[current])  # add len of connected nodes

            for neighbour in graph[current]:
                if not visited[neighbour]:
                    stk.append(neighbour)

        # Complete graph: e=n(n-1)/2
        if node_count * (node_count - 1) == edge_count:
            result += 1

    return result


def _test_case(n: int, edges: List[List[int]], expected: int) -> None:
    """Run a test case for the count_complete_components function

    Args:
        n (int): The number of nodes in the graph
        edges (List[List[int]]): The edges of the graph
        expected (int): The expected result
    """
    result: str = "pass" if count_complete_components(n, edges) == expected else "fail"
    print(f"Test Case: {result}")


def main() -> None:
    print("2685. Count the Number of Complete Components")

    edges_1: List[List[int]] = [[0, 1], [0, 2], [1, 2], [3, 4]]
    _test_case(6, edges_1, 3)

    edges_2: List[List[int]] = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    _test_case(6, edges_2, 1)


if __name__ == "__main__":
    main()
