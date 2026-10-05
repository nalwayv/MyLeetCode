#include "string.h"
#include "stdio.h"

static int check_valid_string(const char* s) {
    const int n = (int)strlen(s);

    int mn = 0;
    int mx = 0;

    for(int i = 0; i < n; i++) {
        const char current = s[i];
        if (current == '(') {
            mn++;
            mx++;
        }

        if (current == ')') {
            mn--;
            mx--;
        }

        // because * can be both '(' and ')'
        if (current == '*') {
            mn--;
            mx++;
        }

        // min can not be negative
        if (mn < 0) {
            mn = 0;
        }

        // if max is negative then there are too many ')'
        if (mx < 0) {
            return 0;
        }
    }

    return mn == 0;
}

int main(void) {
    printf("678. Valid Parenthesis String");

    int result = check_valid_string("(*))");
    printf("(*)) is valid? %s\n", result == 1 ? "Pass": "Fail");
}
