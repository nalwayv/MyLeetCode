#include <stdlib.h>
#include <string.h>

/*
 *  32. Longest Valid Parentheses
 */
int longestValidParentheses(char* s) {
    const int n = (int)strlen(s);

    int top = -1;
    int* stack = malloc((size_t)(n + 1) * sizeof(int));
    stack[++top] = -1;

    int max_len = 0;
    for (int i = 0; i < n; i++) {

        if (s[i] == '(') {
            stack[++top] = i;
        } else {
            top--;

            if (top + 1 == 0) {
                stack[++top] = i;
            } else {
                const int len = i - stack[top];
                if (len > max_len) {
                    max_len = len;
                }
            }
        }
    }

    free(stack);

    return max_len;
}