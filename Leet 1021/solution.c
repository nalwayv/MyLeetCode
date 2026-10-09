#include <string.h>
#include <stdlib.h>

/*
 * 1021. Remove Outermost Parentheses
 * @param s - c string
 * @returns an updated new cstring of s
 * @note needs to be freed
 */
char* remove_outer_parentheses(char* s) {
    const int n = (int)strlen(s);

    int top = -1;
    char* buffer = malloc((size_t)(n));

    int depth = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            if (depth > 0) {
                buffer[++top] = '(';
            }
            depth++;
        } else {
            depth--;
            if (depth > 0) {
                buffer[++top] = ')';
            }
        }
    }

    // create new cstring
    const int length = top + 1;
    char* result_cst = malloc(length + 1);
    memcpy(result_cst, buffer, length);
    result_cst[length] = '\0';

    free(buffer);

    return result_cst;
}
