class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        result: int = 0

        for i in range(len(points) - 1):
            a: list[int] = points[i]
            b: list[int] = points[i+1]

            dx: int = abs(a[0] - b[0])
            dy: int = abs(a[1] - b[1])

            lo: int = min(dx, dy)
            hi: int = max(dx, dy)
            
            dist: int = lo + (hi - lo)

            result += dist

        return result


def main() -> None:
    print('1266. Minimum Time Visiting All Points')
    solution = Solution()
    pts = [[1,1],[3,4],[-1,0]]
    case1 = solution.minTimeToVisitAllPoints(pts)
    print(case1)


if __name__ == '__main__':
    main()