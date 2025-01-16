from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        """Chech if these is a valid path from source to destination.
        """
        # build graph from edges
        graph: dict[int, list[int]] = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])

            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])

        # bfs
        visited: set[int] = set()
        que: deque[int] = deque()
        que.append(source)
        
        while que:
            current: int = que.popleft()
            if current == destination:
                return True
            
            for node in graph[current]:
                if node not in visited:
                    visited.add(node)
                    que.append(node)

        return False


def case1(sol: Solution) -> None:
    edges: list[list[int]] = [[0,1],[1,2],[2,0]]
    n: int = len(edges)
    source: int = 0
    destination: int = 2
    result = sol.validPath(n, edges, source, destination)
    print(f"Case 1: {result} == True")


def case2(sol: Solution) -> None:
    edges: list[list[int]] = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    n: int = len(edges)
    source: int = 0
    destination: int = 5
    result = sol.validPath(n, edges, source, destination)
    print(f"Case 2: {result} == False")


def case3(sol: Solution) -> None:
    edges: list[list[int]] = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    n: int = len(edges)
    source: int = 5
    destination: int = 9
    result = sol.validPath(n, edges, source, destination)
    print(f"Case 3: {result} == True")


def main() -> None:
    print("1971. Find if Path Exists in Graph")

    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()