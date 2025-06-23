int* leftRightDifference(int* nums, int numsSize, int* returnSize) 
{
    int* result = calloc(numsSize, sizeof(int));
    *returnSize = numsSize;
    
    int left = 0;
    int right = 0;
    for(int i = 1; i < numsSize; i++) 
    {
        right += nums[i];
    }
    
    for(int i = 0; i < numsSize; i++) 
    {
        result[i] = abs(left - right);
        
        left += nums[i];

        if (i + 1 < numsSize)
        {
            right -= nums[i+1];
        }
    }
    
    return result;
}