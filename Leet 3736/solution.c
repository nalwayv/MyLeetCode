#include <stdio.h>

#define ARRAY_LENGTH(a) (sizeof(a) / sizeof((a)[0]))

int minMoves(int* nums, int numsSize) {
    int max_number = nums[0];
    for(int i = 1; i < numsSize; i++) {
        max_number = max_number > nums[i] ? max_number : nums[i];
    }

    int moves = 0;
    for(int i = 0; i < numsSize; i++) {
        moves += (max_number - nums[i]);
    }

    return moves;
}

int main(void) {
    printf("3736. Minimum Moves to Equal Array Elements III");

    int nums[] = {2, 1, 3};
    const int result = minMoves(nums, ARRAY_LENGTH(nums));
    printf("Min Moves for [2,1,3] = %d\n", result);

    return 0;
}
