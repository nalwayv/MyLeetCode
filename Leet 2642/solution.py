import heapq


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.graph: dict[int, dict[int, int]] = {i: {} for i in range(n)}
        for edge in edges:
            if len(edge) != 3:
                continue

            f, t, w = edge
            self.graph[f][t] = w

    def addEdge(self, edge: list[int]) -> None:
        if len(edge) != 3:
            return

        f, t, w = edge
        self.graph[f][t] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        heap: list[tuple[float, int]] = [(0, node1)]
        weights = [float('inf')] * len(self.graph)
        weights[node1] = 0

        while heap:
            weight, value = heapq.heappop(heap)

            if value == node2:
                return int(weight)
            
            if weight > weights[value]:
                continue
            
            for neighbour_value, neighbour_weight in self.graph[value].items():
                new_weight: float = weight + neighbour_weight
                if weights[neighbour_value] > new_weight:
                    weights[neighbour_value] =new_weight
                    heapq.heappush(heap, (weights[neighbour_value], neighbour_value))
        return -1


def main() -> None:
    print("2642. Design Graph With Shortest Path Calculator")

    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(g.shortestPath(3, 2))     # return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
    print(g.shortestPath(0, 3))     # return -1. There is no path from 0 to 3.
    g.addEdge([1, 3, 4])            # We add an edge from node 1 to node 3, and we get the second diagram above.
    print(g.shortestPath(0, 3))     # return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.


if __name__ == "__main__":
    main()