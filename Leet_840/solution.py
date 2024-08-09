class Solution:
    def is_magic(self, grid: list[list[int]], startx: int, starty: int) -> bool:
        for x in range(startx, startx + 3):
            t: int = 0
            t += grid[x][starty+0]
            t += grid[x][starty+1]
            t += grid[x][starty+2]
            if t != 15:
                return False
        
        for y in range(starty, starty + 3):
            t: int = 0
            t += grid[startx+0][y]
            t += grid[startx+1][y]
            t += grid[startx+2][y]
            if t != 15:
                return False
        
        diagonal_right_left: int = grid[startx][starty] + grid[startx+1][starty+1] + grid[startx+2][starty+2]
        if diagonal_right_left != 15:
            return False
        
        diagonal_left_right: int = grid[startx+2][starty] + grid[startx+1][starty+1] + grid[startx][starty+2]
        if diagonal_left_right != 15:
            return False

        return True

    def check_if_cell_is_magic(self, grid: list[list[int]], startx: int, starty: int) -> bool:
        row: int = len(grid)
        col: int = len(grid[0])

        # check if cell uses all numbers from 1 to 9

        set_numbers: set[int] = set(range(1, 10))

        for x in range(startx, startx + 3):
            for y in range(starty, starty + 3):

                if not (x >= 0 and x < row and y >= 0 and y < col):
                    continue
                
                if grid[x][y] not in set_numbers:
                    return False
                    
                set_numbers.remove(grid[x][y])

        # could use all numbers but not be magic
        
        if len(set_numbers) == 0 and self.is_magic(grid, startx, starty):
            return True
        
        return False

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        row: int = len(grid)
        col: int = len(grid[0])

        count: int = 0
        for x in range(row):
            for y in range(col):
                if self.check_if_cell_is_magic(grid, x, y):
                    count += 1
        return count


def main() -> None:
    print("840. Magic Squares In Grid")

    sol = Solution()

    grid = [
        [4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
    
    print(sol.numMagicSquaresInside(grid) == 1)
    
    grid2 = [
        [4,3,8,4,5,7],
        [9,5,1,9,8,1],
        [2,7,6,2,3,6],
        [2,7,6,2,9,7],
        [9,5,1,1,3,4],
        [4,3,8,5,8,6]]

    print(sol.numMagicSquaresInside(grid2) == 2)


if __name__ == "__main__":
    main()