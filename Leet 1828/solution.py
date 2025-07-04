class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        result: list[int] = []

        for query in queries:
            count: int = 0

            for point in points:
                # check point is inside circle
                if pow(point[0] - query[0], 2) + pow(point[1] - query[1], 2) <= pow(query[2], 2):
                    count += 1

            result.append(count)

        return result
    

def main() -> None:
    print("1828. Queries on Number of Points Inside a Circle")
    sol = Solution()
    print(sol.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]))
    print(sol.countPoints([[1,1],[2,2],[3,3],[4,4],[5,5]], [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]))


if __name__ == "__main__":
    main()