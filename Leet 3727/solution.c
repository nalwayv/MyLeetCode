#include <stdlib.h>
#include <string.h>

static int int_abs_compare(const void* x, const void* y) {
    int a = *(const int*)x;
    int b = *(const int*)y;

    a = abs(a);
    b = abs(b);

    return (a > b) - (a < b);
}

// 3727. Maximum Alternating Sum of Squares
static long long maxAlternatingSum(const int* nums, const int numsSize) {
    if (numsSize == 0) {
        return 0;
    }

    int* cpy = malloc(sizeof(int) * numsSize);
    memcpy(cpy, nums, sizeof(int) * numsSize);

    qsort(cpy, numsSize, sizeof(int), int_abs_compare);

    size_t i = 0;
    size_t j = numsSize - 1;
    long long result = 0;

    while (i < j) {
        result += (long long)cpy[j] * cpy[j];
        result -= (long long)cpy[i] * cpy[i];
        i++;
        j--;
    }

    if (i == j) {
        result += cpy[i] * cpy[i];
    }

    free(cpy);

    return result;
}
