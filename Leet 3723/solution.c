#include <stdlib.h>

/**
 * 3723. Maximize Sum of Squares of Digits.
 *
 * @param num positive int between 1 and 2 * 10^5.
 * @param sum positive int between 1 and 2 * 10^6.
 * @return maximize sum.
 * @remarks this function malloc's a new string that needs to be freed.
 */
static char* max_sum_of_squares(const int num, int sum) {
    int at = 0;
    char* build = malloc(num + 1);

    for (int i = 0; i < num; i++) {
        const char char_nums[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

        const int digit = 9 < sum ? 9 : sum;
        build[at++] = char_nums[digit];
        // build[at++] = (char)(digit + '0');

        sum -= digit;
    }

    build[num] = '\0';

    if (sum > 0) {
        build[0] = '\0';
    }

    return build;
}
