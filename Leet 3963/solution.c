#include <string.h>
#include <stdlib.h>

/**
 * 3963. Create Grid With Exactly One Path
 * @param m rows
 * @param n cols
 * @param returnSize length of returned array
 * @return arrau of strings
 * @note array of strings must be freed if not null.
 */
static char** createGrid(const int m, const int n, int* returnSize) {
    const int rows = m;
    const int cols = n;

    char** arr = malloc(rows * sizeof(char*));
    if (arr == NULL) {
        goto fail;
    }

    for (int i = 0; i < rows; i++) {
        arr[i] = malloc(cols + 1);
        if (arr[i] == NULL) {
            goto cleanup;
        }

        if (i == 0) {
            memset(arr[i],'.', cols);
        } else {
            memset(arr[i], '#', cols - 1);
            arr[i][cols-1] = '.';
        }

        arr[i][cols] = '\0';
    }

    *returnSize = rows;
    return arr;

cleanup:
    for (int i = 0; i < rows; i++) {
        if (arr[i] != NULL) {
            free(arr[i]);
        }
    }
    free(arr);

fail:
    *returnSize = 0;
    return NULL;
}
