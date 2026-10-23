#include <stdio.h>

/**
 * @params nums 0 <= nums[i] <= n - 1
 * @params numsSize 1 <= n == nums.length <= 105
 * @returns maximum value of k such that the array can be sorted in non-decreasing order .
 */
static int sort_permutation(int* nums, int numsSize) {
    int result = -1;

    for(int i = 0; i < numsSize; i++) {
        if (nums[i] == i) {
            continue;
        }

        if (result == -1) {
            result = nums[i];
        } else {
            result &= nums[i];
        }
    }

    return (result == -1) ? 0 : result;
}

#define ARRAY_LENGTH(arr) (sizeof(arr) / sizeof((arr)[0]))

int main(void) {
    printf("3644. Maximum K to Sort a Permutation");

    int nums[] = {0,3,2,1};
    int result = sort_permutation(nums, ARRAY_LENGTH(nums));

    printf("Result: %d\n", result);

    return 0;
}
