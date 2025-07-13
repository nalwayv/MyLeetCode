class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        """
        Rotates a box represented as a 2D grid 90 degrees clockwise after simulating gravity.
        Each cell in the grid can be:

            . '#' - a stone that can fall down,
            . '.' - an empty space,
            . '*' - an obstacle that blocks stones from falling.

        The function first simulates gravity so that all stones fall as far right as possible in each row, stopping at obstacles or the edge. Then, it rotates the box 90 degrees clockwise and returns the resulting grid.
        
        Args:
            boxGrid (list[list[str]]): The original 2D grid representing the box.
       
         Returns:
            list[list[str]]: The 2D grid after simulating gravity and rotating 90 degrees clockwise.
        """
        rows: int = len(boxGrid)
        cols: int = len(boxGrid[0])

        # create a copy to not destory the original
        copy: list[list[str]] = []
        for row in range(rows):
            r: list[str] = []
            for col in range(cols):
                r.append(boxGrid[row][col])
            copy.append(r)

        # move falling cells if they are not blocked
        for row in range(rows):
            column: list[str] = copy[row]
            j: int = 0
            for i in range(cols):
                if column[i] == "*":
                    j = i + 1
                elif column[i] != "#":
                    column[j], column[i] = column[i], column[j]
                    j += 1

        # create rotated 90 clockwise result
        result: list[list[str]] = []
        for col in range(cols):
            arr: list[str] = []
            for row in range(rows):
                arr.append(copy[rows - row - 1][col])
            result.append(arr)
    
        return result


def print_grid(grid: list[list[str]]) -> None:
    rows: int = len(grid)
    cols: int = len(grid[0])

    for row in range(rows):
        print("[",end="")
        for col in range(cols):
            print(f" {grid[row][col]} ", end="")
        print("]")


def main() -> None:
    print("1861. Rotating the Box")

    sol = Solution()

    print("case 1")
    box_grid_1 = [["#",".","#"]]
    print_grid(box_grid_1)
    print_grid(sol.rotateTheBox(box_grid_1))

    print("case 2")
    box_grid_2 = [
        ["#",".","*","."],
        ["#","#","*","."]]
    print_grid(sol.rotateTheBox(box_grid_2))

    print("case 3")
    box_grid_3 = [
        ["#","#","*",".","*","."],
        ["#","#","#","*",".","."],
        ["#","#","#",".","#","."]]
    print_grid(sol.rotateTheBox(box_grid_3))

    print("case 4")
    box_grid_4 = [["*","#","*",".",".",".","#",".","*","."]]
    print_grid(sol.rotateTheBox(box_grid_4))


if __name__ == "__main__":
    main()