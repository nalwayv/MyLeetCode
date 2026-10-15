#include <stdlib.h>
#include <string.h>
#include <stdint.h>


static int int_abs_compare(const void* x, const void* y) {
    int a = *(const int*)x;
    int b = *(const int*)y;

    a = abs(a);
    b = abs(b);

    return (a > b) - (a < b);
}


// 3727. Maximum Alternating Sum of Squares
static int64_t maxAlternatingSum(const int* nums, const int numsSize) {
    if (numsSize == 0) {
        return 0;
    }

    int* cpy = malloc(sizeof(int) * numsSize);
    memcpy(cpy, nums, sizeof(int) * numsSize);

    qsort(cpy, numsSize, sizeof(int), int_abs_compare);

    int64_t result = 0;

    for(size_t lo = 0; lo < numsSize / 2; lo++) {
        size_t hi = numsSize - lo - 1;

        result += (int64_t)cpy[hi] * cpy[hi];
        result -= (int64_t)cpy[lo] * cpy[lo];
    }

    if (numsSize % 2 == 1) {
        size_t mid = numsSize / 2;
        result += (int64_t)cpy[mid] * cpy[mid];
    }

    free(cpy);

    return result;
}
