class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Finds all coordinates in the given matrix where water can flow to both the Pacific and Atlantic oceans.
        Water can flow from a cell to another cell if the next cell's height is equal to or lower than the current cell's height.
        The Pacific ocean touches the left and top edges of the matrix, and the Atlantic ocean touches the right and bottom edges.
        Args:
            heights (list[list[int]]): A 2D matrix representing the heights of each cell.
        Returns:
            list[list[int]]: A list of coordinates [row, col] where water can flow to both the Pacific and Atlantic oceans.
        """
        rows: int = len(heights)
        cols: int = len(heights[0])

        dirs: list[tuple[int, int]] = [(1,0), (0,-1), (-1,0), (0,1)]

        # borders
        pacific: list[tuple[int, int]] = []
        atlantic: list[tuple[int, int]] = []
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.append((r,c))

                if r == rows - 1 or c == cols - 1:
                    atlantic.append((r,c))

        # pacific
        seen_p: list[list[bool]] = [[False for _ in range(cols)] for _ in range(rows)]
        for px,py in pacific:
            seen_p[px][py] = True

        stk_p: list[tuple[int, int]] = pacific
        while stk_p:
            cx,cy = stk_p.pop()

            for dx,dy in dirs:
                nx: int = cx + dx
                ny: int = cy + dy

                if 0 <= nx < rows and 0 <= ny < cols and not seen_p[nx][ny] and heights[nx][ny] >= heights[cx][cy]:
                    seen_p[nx][ny] = True
                    stk_p.append((nx, ny))

        # atlantic
        seen_a: list[list[bool]] = [[False for _ in range(cols)] for _ in range(rows)]
        for ax,ay in atlantic:
            seen_a[ax][ay] = True

        stk_a: list[tuple[int, int]] = atlantic
        while stk_a:
            cx,cy = stk_a.pop()

            for dx,dy in dirs:
                nx: int = cx + dx
                ny: int = cy + dy

                if 0 <= nx < rows and 0 <= ny < cols and not seen_a[nx][ny] and heights[nx][ny] >= heights[cx][cy]:
                    seen_a[nx][ny] = True
                    stk_a.append((nx, ny))

        # combine
        result: list[list[int]] = []
        for r in range(rows):
            for c in range(cols):
                if seen_p[r][c] and seen_a[r][c]:
                    result.append([r,c])
    
        return result
        

def main() -> None:
    print('417. Pacific Atlantic Water Flow')

    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4],
    ]
    solution = Solution()
    for coord in solution.pacificAtlantic(heights):
        print(*coord, sep=',')


if __name__ == '__main__':
    main()