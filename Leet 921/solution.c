#include <stdio.h>

int min_add_to_make_valid(char* s) {
    int unbalanced = 0;
    int top = 0;

    for(int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            top++;
        } else {
            if (top > 0) {
                top--;
            } else {
                unbalanced++;
            }
        }
    }
    
    return top + unbalanced;
}

int main(void) {
    printf("921. Minimum Add to Make Parentheses Valid\n");

    const int result = min_add_to_make_valid("())");
    printf("- ()) equals %d\n", result);

    return 0;
}