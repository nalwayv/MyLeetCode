#include <stdlib.h>
#include <stdbool.h>


static int sum_digits(int number) {
    int result = 0;
    while (number > 0) {
        result += number % 10;
        number /= 10;
    }
    return result;
}


typedef struct {
    int sum_digits;
    int original_value;
    size_t original_index;
} MinSwapNode;


static int min_swap_compare(const void* a, const void* b) {
    const MinSwapNode* node_a = a;
    const MinSwapNode* node_b = b;

    int result = 0;
    if (node_a->sum_digits == node_b->sum_digits) {
        result = (node_a->original_value > node_b->original_value) - (node_a->original_value < node_b->original_value);
    } else {
        result = (node_a->sum_digits > node_b->sum_digits) - (node_a->sum_digits < node_b->sum_digits);
    }
    return result;
}


/**
 * 3551. Minimum Swaps to Sort by Digit Sum
 *
 * @param nums
 * @param nums_length
 * @return min number of swaps
 */
int min_swaps(int* nums, int numsSize) {
    MinSwapNode* nodes = malloc(sizeof(MinSwapNode) * numsSize);
    for (size_t i = 0; i < numsSize; i++) {
        nodes[i] = (MinSwapNode) {
            .sum_digits = sum_digits(nums[i]),
            .original_value = nums[i],
            .original_index = i
        };
    }

    qsort(nodes, numsSize, sizeof(MinSwapNode), min_swap_compare);

    bool* visited = malloc(sizeof(bool) * numsSize);
    for (size_t i = 0; i < numsSize; i++) {
        visited[i] = false;
    }

    int cycle = 0;
    for (size_t i = 0; i < numsSize; i++) {
        if (visited[i]) {
            continue;
        }

        cycle++;

        size_t j = i;
        while (!visited[j]) {
            visited[j] = true;
            j = nodes[j].original_index;
        }
    }

    free(nodes);
    free(visited);

    return numsSize - cycle;
}
