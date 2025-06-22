#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char** divideString(char* s, int k, char fill, int* returnSize) 
{
    int n = strlen(s);
    *returnSize = (n + k - 1) / k;
    char** arr = calloc(*returnSize, sizeof(char*));

    int i = 0;
    int p1 = 0;
    int p2 = 0;
    while (p1 < n)
    {
        int j = 0;
        arr[i] = calloc(k, sizeof(char*));
        
        while(p2 < n && j < k)
        {
            arr[i][j] = s[p2];
            j += 1;
            p2 += 1;
        }

        while(j < k)
        {
            arr[i][j] = fill;
            j += 1;
        }
        
        i += 1;
        p1 = p2;
    }
    
    return arr;
}


int main()
{
    printf("2138. Divide a String Into Groups of Size k\n");

    int size = 0;
    char** arr = divideString("abc", 4, 'x', &size);
    
    if (arr)
    {
        for(int i = 0; i < size; i++)
        {
            printf("%s\n", arr[i]);
        }
    }
    
    return 0;
}