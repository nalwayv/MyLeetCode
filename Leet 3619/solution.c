#include <stdlib.h>
#include <stdint.h>

static int grid_in_range(const int rows, const int cols, const int row, const int col) {
    return 0 <= row && row < rows && 0 <= col && col < cols;
}


static uint64_t explore_island(
    int** grid,
    const int rows,
    const int cols,
    const int row,
    const int col,
    int* explored
    ) {
    if (!grid_in_range(rows, cols, row, col) || grid[row][col] == 0 || explored[row * cols + col]) {
        return 0;
    }

    explored[row * cols + col] = 1;

    uint64_t current_sum = grid[row][col];

    current_sum = explore_island(grid, rows, cols, row + 1, col, explored) + current_sum;
    current_sum = explore_island(grid, rows, cols, row - 1, col, explored) + current_sum;
    current_sum = explore_island(grid, rows, cols, row, col + 1, explored) + current_sum;
    current_sum = explore_island(grid, rows, cols, row, col - 1, explored) + current_sum;

    return current_sum;
}

/**
 * 3619. Count Islands With Total Value Divisible by K
 */
int countIslands(int** grid, int gridSize, int* gridColSize, int k) {
    const int rows = gridSize;
    const int cols = *gridColSize;

    int* explored = calloc(rows * cols, sizeof(int));
    if (explored == NULL) {
        return 0;
    }

    int count = 0;

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (grid[row][col] > 0 && explored[row * cols + col] == 0) {
                if (explore_island(grid, rows, cols, row, col, explored) % k == 0) {
                    count++;
                }
            }
        }
    }

    free(explored);

    return count;
}
