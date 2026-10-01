/** 20. Valid Parentheses */

#include <stdlib.h>

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


static int is_valid_parentheses(const char open, const char close) {
    if (open == '(' && close == ')') {
        return 1;
    }

    if (open == '{' && close == '}') {
        return 1;
    }

    if (open == '[' && close == ']') {
        return 1;
    }

    return 0;
}


static int is_open_parentheses(const char ch) {
    return ch == '(' || ch == '[' || ch == '{';
}


static int check_if_parentheses_is_valid(struct stack* stk, const char* cstring) {
    for (int i = 0; cstring[i] != '\0'; i++) {
        const char current_char = cstring[i];

        if (is_open_parentheses(current_char)) {
            stack_push(stk, current_char);
        } else {
            if (!stack_is_empty(stk) && is_valid_parentheses(stack_peek(stk), current_char)) {
                stack_pop(stk);
            } else {
                return 0;
            }
        }
    }

    return stack_is_empty(stk);
}


/**
 * Check if string s has valid parentheses usage.
 * @param cstring string comprised of () [] {}
 * @return 1 if valid else 0 if not.
 */
int is_valid(char* s) {
    int len = 0;
    while (cstring[len] != '\0') {
        len++;
    }

    struct stack stk = stack_create(len);
    const int result = check_if_cstring_parentheses_is_valid(&stk, cstring);
    
    stack_delete(&stk);
    
    return result;
}