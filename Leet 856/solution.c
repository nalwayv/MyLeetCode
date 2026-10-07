#include <string.h>
#include <stdlib.h>
#include <stdio.h>


/*
 * Return the score for a balanced parentheses string consisting of '(' and ')'.
 * @param s c string
 * @returns int score
 */
int score_of_parentheses(const char* s) {
    const int n = (int)strlen(s);

    int top = -1;
    int* stack = malloc((size_t)(n + 1) * sizeof(int));
    stack[++top] = 0;

    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            stack[++top] = 0;
        } else {
            const int value = stack[top--];
            stack[top] += (value == 0) ? 1 : 2 * value;
        }
    }

    const int result = stack[top];
    free(stack);

    return result;
}


int main(void) {
    printf("856. Score of Parentheses\n");

    const int score = score_of_parentheses("(())");
    printf("Score for (()) = %d\n", score);

    return 0;
}
