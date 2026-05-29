//////////////////////
// 1306. Jump Game III

#define MAX_SIZE 50000

typedef struct stack 
{ 
    int top; 
    int values[MAX_SIZE];
} Stack;

int StackIsEmpty(Stack* stk) 
{
    return stk->top == -1;
}

void StackPush(Stack* stk, int val)
{
    if (stk->top < MAX_SIZE - 1)
    {
        stk->top++;
        stk->values[stk->top] = val;
    }
}

void StackPop(Stack* stk) 
{
    if(stk->top >= 0 ) 
    {
        stk->top--;
    }
}

int StackTop(Stack* stk)
{
    return stk->values[stk->top];
}

bool canReach(int* arr, int arrSize, int start)
 {
    Stack stk;
    stk.top = -1;

    int seen[MAX_SIZE];
    for(int i = 0; i < MAX_SIZE; i++) 
        seen[i] = 0;

    StackPush(&stk, start);

    while (!StackIsEmpty(&stk))
    {
        int current = StackTop(&stk);
        StackPop(&stk);

        if(seen[current] == 1) 
            continue;

        seen[current] = 1;

        if (0 <= current && current < arrSize) 
        {
            if(arr[current] == 0) 
                return true;
            
            int add = current + arr[current];
            if(add >= 0 && add < MAX_SIZE)
                StackPush(&stk, add);

            int sub = current - arr[current];
            if(sub >= 0 && sub < MAX_SIZE)
                StackPush(&stk, sub);
        }
    }

    return false;
}