#include <ctype.h>

static int string_to_int(const char* str, const size_t len,  const int lo,  const int hi) {
    if (str == NULL || lo < 0 || hi >= (int)len || lo > hi) {
        return 0;
    }

    int result = 0;
    for (size_t i = lo; i <= hi; i++) {
        const char current = str[i];
        if (isdigit(current)) {
            result = result * 10 + (current - '0');
        } else {
            return 0;
        }
    }

    return result;
}

static int day_of_year(const char* date, const size_t len) {
    const int month = string_to_int(date, len, 0, 1);
    const int day = string_to_int(date, len, 3, 4);

    if (month > 0 && month <= 12 && day > 0 && day <= 31) {
        const int days_before[] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        return days_before[month - 1] + day;
    }

    return -1;
}

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

/**
 * 2409. Count Days Spent Together
 */
int count_days_together(char* arriveAlice, char* leaveAlice, char* arriveBob, char* leaveBob) {
    const int alice_start = day_of_year(arriveAlice, 5);
    if (alice_start == -1) return 0;

    const int alice_end = day_of_year(leaveAlice, 5);
    if (alice_end == -1) return 0;

    const int bob_start = day_of_year(arriveBob, 5);
    if (bob_start == -1) return 0;

    const int bob_end = day_of_year(leaveBob, 5);
    if (bob_end == -1) return 0;

    return MAX(0, MIN(alice_end, bob_end) - MAX(alice_start, bob_start) + 1);
}
