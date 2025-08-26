class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        """
        Calculates the area of the row in the given 2D list whose diagonal (Euclidean norm) is the longest.
        For each row in `dimensions`, computes the Euclidean norm (square root of the sum of squares of elements)
        and the area (product of all elements in the row). Returns the area of the row with the longest diagonal.
        If multiple rows have the same maximum diagonal length, returns the largest area among them.
        Args:
            dimensions (list[list[int]]): A 2D list where each inner list represents dimensions of a shape.
        Returns:
            int: The area (product of elements) of the row with the longest diagonal.
        """

        rows: int = len(dimensions)
        cols: int = len(dimensions[0])
        
        max_length: float = 0.0
        max_area: int = 0

        for x in range(rows):
            length: float = 0.0
            area: int = 1

            for y in range(cols):
                length += pow(dimensions[x][y], 2)
                area *= dimensions[x][y]
            
            sq_length: float = length ** 0.5
            if sq_length > max_length:
                max_length = sq_length
                max_area = area
            elif sq_length == max_length:
                max_area = max(max_area, area)

        return max_area


def main() -> None:
    print("3000. Maximum Area of Longest Diagonal Rectangle")
    
    sol = Solution()
    
    grid1: list[list[int]] = [[9,3], [8,6]]
    case1: int = sol.areaOfMaxDiagonal(dimensions=grid1)
    print(f"case 1 should equal 48 ? {case1}")

    grid2: list[list[int]] = [[3,4],[4,3]]
    case2: int = sol.areaOfMaxDiagonal(dimensions=grid2)
    print(f"case 2 should equal 12 ? {case2}")

    grid3: list[list[int]] = [
        [6,5],
        [8,6],
        [2,10],
        [8,1],
        [9,2],
        [3,5],
        [3,5]]
    case3: int = sol.areaOfMaxDiagonal(dimensions=grid3)
    print(f"case 3 should equal 20 ? {case3}")

    grid4: list[list[int]] = [
        [4,7],[8,9],[5,3],[6,10],[2,9],
        [3,10],[2,2],[5,8],[5,10],[5,6],
        [8,9],[10,7],[8,9],[3,7],[2,6],
        [5,1],[7,4],[1,10],[1,7],[6,9],
        [3,3],[4,6],[8,2],[10,6],[7,9],
        [9,2],[1,2],[3,8],[10,2],[4,1],
        [9,7],[10,3],[6,9],[9,8],[7,7],
        [5,7],[5,4],[6,5],[1,8],[2,3],
        [7,10],[3,9],[5,7],[2,4],[5,6],
        [9,5],[8,8],[8,10],[6,8],[5,1],
        [10,8],[7,4],[2,1],[2,7],[10,3],
        [2,5],[7,6],[10,5],[10,9],[5,7],
        [10,6],[4,3],[10,4],[1,5],[8,9],
        [3,1],[2,5],[9,10],[6,6],[5,10],
        [10,2],[6,10],[1,1],[8,6],[1,7],
        [6,3],[9,3],[1,4],[1,1],[10,4],
        [7,9],[4,5],[2,8],[7,9],[7,3],
        [4,9],[2,8],[4,6],[9,1],[8,4],
        [2,4],[7,8],[3,5],[7,6],[8,6],
        [4,7],[25,60],[39,52],[16,63],[33,56]]
    case4: int = sol.areaOfMaxDiagonal(dimensions=grid4)
    print(f"case 4 should equal 2028 ? {case4}")


if __name__ == "__main__":
    main()
        