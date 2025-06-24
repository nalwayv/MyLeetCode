int* findKDistantIndices(int* nums, int numsSize, int key, int k, int* returnSize) 
{
    int* keys = calloc(numsSize, sizeof(int));
    int keysSize = 0;
    for(int i = 0; i < numsSize; i++)
    {
        if (nums[i] == key)
        {
            keys[keysSize++] = i;
        }
    }

    int j = 0;
    int* result = calloc(numsSize, sizeof(int));
    int resultSize = 0;
    for(int i = 0; i < numsSize; i++)
    {
        while (j < keysSize && keys[j] < i - k)
        {
            j++;
        }
        
        if (j < keysSize && abs(keys[j] - i) <= k)
        {
            result[resultSize++] = i;
            *returnSize = resultSize;
        }
    }

    free(keys);
    return result;
}