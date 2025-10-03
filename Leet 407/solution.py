import heapq


def trap_rain_water(heights: list[list[int]]) -> int:
    rows: int = len(heights)
    cols: int = len(heights[0])
    heap: list[tuple[int, int, int]] = []
    seen: list[list[bool]] = [[False] * cols for _ in range(rows)]

    # Push boundary cells
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                heapq.heappush(heap, (heights[r][c], r, c))
                seen[r][c] = True

    total: int = 0
    while heap:
        current_height, x, y = heapq.heappop(heap)
        
        for dx, dy in [(1,0), (0,-1), (-1,0), (0,1)]:    
            nx: int = x + dx
            ny: int = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not seen[nx][ny]:
                seen[nx][ny] = True
                neighbour_height = heights[nx][ny]

                total += max(0, current_height - neighbour_height)
                heapq.heappush(heap, (max(current_height, neighbour_height), nx, ny))

    return total


def main() -> None:
    print('407. Trapping Rain Water II')
    heights = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    print(trap_rain_water(heights) == 4)


if __name__ == '__main__':
    main()