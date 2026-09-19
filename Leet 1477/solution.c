#include <stdlib.h>

#define min(a, b) (((a) < (b)) ? (a) : (b))

int minSumOfLengths(int* arr, int arrSize, int target) 
{
    int maxWindowSize = arrSize + 1;

    int* dp = calloc(sizeof(int), arrSize + 1);
    for (int i = 0; i <= arrSize; i++)
    {
        dp[i] = maxWindowSize;
    }

    int result = maxWindowSize;
    int total = 0;
    
    int left = 0;
    
    for(int right = 0; right < arrSize; right++)
    {
        total += arr[right];

        while (total > target)
        {
            total -= arr[left++];
        }

        dp[right + 1] = dp[right];

        if (total == target)
        {
            int currentWindow = right - left + 1;
            dp[right + 1] = min(dp[right + 1], currentWindow);

            result = min(result, dp[left] + currentWindow);
        }
    }

    free(dp);
    
    return result != maxWindowSize ? result : -1;
}

