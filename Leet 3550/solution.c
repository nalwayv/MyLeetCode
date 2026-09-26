#include <stdio.h>

static int sum_digits(int num) {
    int result = 0;
    while (num > 0) {
        result += (num % 10);
        num /= 10;
    }
    return result;
}

static int smallest_index(int* nums, int nums_size) {
    for(int i = 0; i < nums_size; i++) {
        if (sum_digits(nums[i]) == i) {
            return i;
        }
    }
    return -1;
}

int main() {
    printf("3550. Smallest Index With Digit Sum Equal to Index");

    int nums[] = {1, 3, 2};
    int nums_size = 3;
    printf("smallest idx with sum digits equal to idx is %d\n", smallest_index(nums, nums_size));

    return 0;
}
