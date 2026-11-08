#include <stdlib.h>

/**
 * 1267. Count Servers that Communicate
 */
static int count_servers(int** grid, const int gridSize, const int* gridColSize)
{
    const int rows = gridSize;
    const int cols = *gridColSize;
    int count = 0;

    int *servers_in_row = calloc((size_t) rows, sizeof(int));
    if (!servers_in_row) {
        return count;
    }

    int *servers_in_col = calloc((size_t) cols, sizeof(int));
    if (!servers_in_col) {
        free(servers_in_row);
        return count;
    }

    // update adjacent
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 1) {
                servers_in_row[i] += 1;
                servers_in_col[j] += 1;
            }
        }
    }

    // count servers that are connected to any other server in ever row or col
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 1 && (servers_in_row[i] > 1 || servers_in_col[j] > 1)) {
                count += 1;
            }
        }
    }

    free(servers_in_row);
    free(servers_in_col);

    return count;
}
