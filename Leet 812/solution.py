from itertools import combinations
class Solution:
    def _get_triangle_area(self, p1: list[int], p2: list[int], p3: list[int]) -> float:
        """
        Calculate the area of a triangle given its three vertices.

        Args:
            p1 (list[int]): The coordinates [x, y] of the first vertex.
            p2 (list[int]): The coordinates [x, y] of the second vertex.
            p3 (list[int]): The coordinates [x, y] of the third vertex.

        Returns:
            float: The absolute value of the area of the triangle formed by the three points.
        """
        area:int = p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
        return abs(area * 0.5)

    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Calculates the largest area of a triangle that can be formed from a list of points.
        Args:
            points (list[list[int]]): A list of points, where each point is represented as a list of two integers [x, y].
        Returns:
            float: The largest area of any triangle that can be formed by any three distinct points from the input list.
        Note:
            This method assumes the existence of a helper method `_get_triangle_area(p1, p2, p3)` that computes the area of a triangle given three points.
        """
        max_area: float = 0.0
        for p1, p2, p3 in combinations(points, 3):
            max_area = max(max_area, self._get_triangle_area(p1, p2, p3))

        return max_area


def main() -> None:
    print('812. Largest Triangle Area')

    solution = Solution()
    
    print('Case 1')
    case1_point = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    case1 = solution.largestTriangleArea(case1_point)
    print(case1)

    print('Case 2')
    case2_point = [[1,0],[0,0],[0,1]]
    case2 = solution.largestTriangleArea(case2_point)
    print(case2)

    print('Case 3')
    case3_point = [[3,0],[0,1],[0,0], [2,1], [3,3], [1,1], [2,2]]
    case3 = solution.largestTriangleArea(case3_point)
    print(case3)


if __name__ == '__main__':
    main()