#include <stdlib.h>
#include <string.h>

static int int_compare(const void* a, const void* b) {
    const int aa = *(const int*)a;
    const int bb = *(const int*)b;
    return (aa > bb) - (aa < bb);
}

/**
 * 2089. Find Target Indices After Sorting Array.
 * Note: The returned array must be malloced, assume caller calls free().
 *
 * @params nums
 * @params numsSize
 * @params target
 * @params returnSize
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    int* sorted_nums = malloc(sizeof(int) * numsSize);
    memcpy(sorted_nums, nums, sizeof(int) * numsSize);
    qsort(sorted_nums, numsSize, sizeof(int), int_compare);

    int* result = malloc(sizeof(int) * numsSize);

    *returnSize = 0;
    for (int i = 0; i < numsSize; i++) {
        if (sorted_nums[i] == target) {
            result[(*returnSize)++] = i;
        }
    }

    free(sorted_nums);

    return result;
}
