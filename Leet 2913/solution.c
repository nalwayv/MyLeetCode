#include <stdbool.h>

/**
 * 2913. Subarrays Distinct Element Sum of Squares I.
 *
 * @param nums int values between 1 and 100.
 * @param nums_length length of nums between 1 and 100.
 * @return sum of the squares of distinct counts of all subarrays of nums.
 */
int sumCounts(int* nums, int numsSize) {
    if (numsSize < 1 || numsSize > 100) {
        return 0;
    }

    int result = 0;
    for (int i = 0; i < numsSize; i++) {
        bool seen[101] = {0};
        int len = 0;

        for (int j = i; j < numsSize; j++) {
            if (nums[j] < 1 || nums[j] > 100) {
                return 0;
            }

            if (seen[nums[j]] == false) {
                seen[nums[j]] = true;
                len++;
            }

            result += len * len;
        }
    }

    return result;
}
