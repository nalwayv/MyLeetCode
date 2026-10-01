#include <stdlib.h>
#include <string.h>
#include <stdio.h>


struct stack {
    char* data;
    int top;
    int capacity;
};


static struct stack stack_create(const int size) {
    return (struct stack) {
        .data = malloc(size),
        .top = -1,
        .capacity = size,
    };
}


static void stack_delete(struct stack* st) {
    free(st->data);
    *st = (struct stack) {0};
}


static void stack_push(struct stack* st, const char c) {
    if (st->top < st->capacity - 1) {
        st->data[++st->top] = c;
    }
}


static char stack_peek(const struct stack* st) {
    return st->data[st->top];
}


static void stack_pop(struct stack* st) {
    if (st->top >= 0 ) {
        st->top--;
    }
}


static void stack_reset(struct stack* st) {
    st->top = -1;
}


static int stack_is_empty(const struct stack* st) {
    return st->top == -1;
}


static char* reverse_parentheses(const char* s) {
    const int len = (int)strlen(s);

    struct stack s1 = stack_create(len);
    struct stack s2 = stack_create(len);

    for (int i = 0; i < len; i++) {
        const char current_char = s[i];

        if (current_char == ')') {

            stack_reset(&s2);

            while (!stack_is_empty(&s1) && stack_peek(&s1) != '(') {
                stack_push(&s2, stack_peek(&s1));
                stack_pop(&s1);
            }

            stack_pop(&s1);

            // copy over
            for (int j = 0; j <= s2.top; j++) {
                stack_push(&s1, s2.data[j]);
            }

        } else {
            stack_push(&s1, current_char);
        }
    }

    // create result string. + 2 for <= top and \0
    char* new_cstring = malloc(s1.top + 2);
    for (int j = 0; j <= s1.top; j++) {
        new_cstring[j] = s1.data[j];
    }
    new_cstring[s1.top + 1] = '\0';

    // clean up
    stack_delete(&s1);
    stack_delete(&s2);

    return new_cstring;
}


int main(void) {
    printf("1190. Reverse Substrings Between Each Pair of Parentheses");

    const char* result = reverse_parentheses("(u(love)i)");
    printf("(u(love)i) -> %s\n", result);
    
    return 0;
}