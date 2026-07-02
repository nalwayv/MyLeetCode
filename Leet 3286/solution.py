from typing import List, Tuple, Dict
import heapq
from sys import maxsize


def findSafeWalk(grid: List[List[int]], health: int) -> bool:
    """Given an m x n binary matrix grid and an integer health check if a path from 0,0 to 
    rows-1, cols-1 is possible.

    cells that equal 1 are unsafe and will decrease health while 0 are safe.
    """
    rows: int = len(grid)
    cols: int = len(grid[0])

    # up, down, left, right
    direction: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    # start at (0,0) with cost grid[0][0]
    cost: Dict[Tuple[int, int], int] = {(0, 0): grid[0][0]}

    # priority queue (cost, xpos, ypos) using heapq
    pq: List[Tuple[int, int, int]] = [(grid[0][0], 0, 0)]
    
    # update min path cost from (0,0) to (rows-1, cols-1)
    while pq:
        _, cx, cy = heapq.heappop(pq)
        current_cost: int = cost[(cx, cy)]
        
        for dx, dy in direction:
            nx: int = cx + dx
            ny: int = cy + dy

            # is nx, ny on grid
            if 0 <= nx < rows and 0 <= ny < cols:
                grid_cost: int = grid[nx][ny]
                next_cost: int = cost.get((nx, ny), maxsize)
    
                if current_cost + grid_cost < next_cost:
                    cost[(nx, ny)] = current_cost + grid_cost
                    heapq.heappush(pq, (cost[(nx, ny)], nx, ny))

    return cost[rows - 1, cols - 1] < health


def main() -> None:
    print("3286. Find a Safe Walk Through a Grid")

    grid1: List[List[int]] = [
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,0]]
    print(findSafeWalk(grid1, 1))

    grid2: List[List[int]] = [
        [0,1,1,0,0,0],
        [1,0,1,0,0,0],
        [0,1,1,1,0,1],
        [0,0,1,0,1,0]]
    print(findSafeWalk(grid2, 3))

    grid3: List[List[int]] = [
        [1,1,1],
        [1,0,1],
        [1,1,1]]
    print(findSafeWalk(grid3, 5))


if __name__ == "__main__":
    main()
