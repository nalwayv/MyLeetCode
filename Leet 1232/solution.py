class Solution:
    def _get_triangle_area(self, p1: list[int], p2: list[int], p3: list[int]) -> float:
        """Return area of a triangle 1/2( p1x(p2y - p3y) + p2x(p3y - p1y) + p3x(p1y - p2y) )
        """
        x:int = 0
        y:int = 1
        area:int = p1[x] * (p2[y] - p3[y]) + p2[x] * (p3[y] - p1[y]) + p3[x] * (p1[y] - p2[y])
        return area * 0.5

    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        """Check if coordinates form a straight line
        """
        n:int = len(coordinates)

        if n <= 1:
            return False
            
        if n == 2:
            return True

        #first 2 points make a straight line
        a:list[int] = coordinates[0]
        b:list[int] = coordinates[1]

        for i in range(2, n):
            #to be collinear area of tri must equal 0
            if self._get_triangle_area(a, b, coordinates[i]) != 0.0:
                return False
        return True


def main() -> None:
    print("1232. Check If It Is a Straight Line")

    sol = Solution()

    coords1:list[list[int]] = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    print(f"case 1 { "pass" if sol.checkStraightLine(coords1) else "fail" }")

    coords2:list[list[int]] = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    print(f"case 2 { "pass" if not sol.checkStraightLine(coords2) else "fail" }")

    coords3:list[list[int]] = [[0,0],[0,1],[0,-1]]
    print(f"case 3 { "pass" if sol.checkStraightLine(coords3) else "fail" }")

    coords4:list[list[int]] = [[2,4],[2,5],[2,8]]
    print(f"case 4 { "pass" if sol.checkStraightLine(coords4) else "fail" }")


if __name__ == "__main__":
    main()