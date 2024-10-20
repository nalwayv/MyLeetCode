class Solution:
    def _count_alive_neighbours(self, board: list[list[int]], i: int, j: int):
        """ 
        count the eight neighbours around current cell and return count 
        of those that are alive.
        """
        # C: current
        # D: dead
        # A: alive
        #
        # A A D
        # D C D
        # D D D
        #
        # count = 2

        rows: int = len(board)
        cols: int = len(board[0])
        count: int = 0

        # check neighbours around cell
        # that are within range on board
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x == i and y == j:
                    continue
                
                if x >= 0 and x < rows and y >= 0 and y < cols:
                    count += board[x][y]

        return count

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows: int = len(board)
        cols: int = len(board[0])
        values: list[int] = [0 for _ in range(rows * cols)]

        dead: int = 0
        alive: int = 1

        for i in range(rows):
            for j in range(cols):
                alive_neighbours: int = self._count_alive_neighbours(board, i, j)

                # game of life conditions
                # 1. any live cell with fewer then two live neighbours dies
                # 2. any live cell with two live neighbours lives
                # 3. any live cell with more than three lives neighbours dies
                # 4. any dead cell with exactly three live neighbours becomes alive again
                if board[i][j] == alive:
                    if alive_neighbours > 3 or alive_neighbours < 2:
                        values[cols * i + j] = dead
                    else:
                        values[cols * i + j] = alive
                else:
                    if alive_neighbours == 3:
                        values[cols * i + j] = alive
                    else:
                        values[cols * i + j] = dead

        # update board
        for i in range(rows):
            for j in range(cols):
                board[i][j] = values[cols * i + j]

        # print board
        for i in range(rows):
            for j in range(cols):
                print(f" {board[i][j]} ",end="")
            print("")


def main() -> None:
    print("289. Game of Life")

    sol = Solution()
    #         c0 c1 c2
    board = [[ 0, 1, 0 ], # r0
             [ 0, 0, 1 ], # r1
             [ 1, 1, 1 ], # r2
             [ 0, 0, 0 ]] # r3

    sol.gameOfLife(board)
    #       [[ 0, 0, 0 ],
    #        [ 1, 0, 1 ],
    #        [ 0, 1, 1 ],
    #        [ 0, 1, 0 ]]


if __name__ == "__main__":
    main()