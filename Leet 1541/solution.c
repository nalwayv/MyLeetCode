#include <string.h>
#include <stdio.h>

int min_insertions(char* s) {
    int n = (int)strlen(s);

    int op = 0;
    int cl = 0;
    int skip_next = 0;

    for(int i = 0; i < n; i++) {
        if (skip_next) {
            skip_next = 0;
            continue;
        }

        if (s[i] == '(') {
            op++;
            continue;
        }

        // )) - skip next
        //  ) - +1
        if (i + 1 < n && s[i + 1] == ')') {
            skip_next = 1;
        } else {
            cl++;
        }


        if (op == 0) {
            cl++;
        } else {
            op--;
        }
    }

    return cl + op * 2;
}

int main(void) {
    printf("1541. Minimum Insertions to Balance a Parentheses String\n");

    const int result_min_insertions = min_insertions("(()))");
    printf("Min insertions result: %d\n", result_min_insertions);

    return 0;
}
