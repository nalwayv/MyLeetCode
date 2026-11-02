#include <stdlib.h>
#include <string.h>

static int cmp(const void* a, const void* b) {
    return (*(const int*)a > *(const int*)b) - (*(const int*)a < *(const int*)b);
}

/**
 * 462. Minimum Moves to Equal Array Elements II
 */
int minMoves2(int* nums, int numsSize) {
    int* sorted = calloc(numsSize, sizeof(*sorted));
    if (!sorted) {
        return 0;
    }
    memcpy(sorted, nums, numsSize * sizeof(*sorted));
    qsort(sorted, numsSize, sizeof(*sorted), cmp);

    int median = sorted[numsSize / 2];

    int moves = 0;
    for(int i = 0; i < numsSize; i++) {
        moves += abs(median - sorted[i]);
    }

    free(sorted);

    return moves;
}
