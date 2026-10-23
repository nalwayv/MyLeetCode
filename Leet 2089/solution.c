#include <stdlib.h>

int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 0;
    if (!nums || numsSize <= 0) {
        return NULL;
    }

    int less = 0;
    int equal = 0;
    for(int i = 0; i < numsSize; i++) {
        if (nums[i] < target) {
            less++;
        } else if(nums[i] == target) {
            equal++;
        }
    }

    if (equal == 0) {
        return NULL;
    }

    int* result = malloc(sizeof(int) * equal);
    if(!result) {
        return NULL;
    }

    for(int i = 0; i < equal; i++) {
        result[i] = less + i;
    }

    *returnSize = equal;
    return result;
}
