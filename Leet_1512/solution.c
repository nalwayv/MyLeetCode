/*
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
*/


int numIdenticalPairs(int* nums, int numsSize) 
{
    /*get max number */
    int maxNumber = -1;
    for(int i = 0; i < numsSize; i++)
    {
        if(nums[i] > maxNumber)
        {
            maxNumber = nums[i];
        }
    }

    /*update frequency table*/
    int count = 0;
    int* table = calloc(maxNumber + 1, sizeof(int));

    for(int i = 0; i < numsSize; i++)
    {
        if(table[nums[i]] == 0)
        {
            table[nums[i]] = 1;
        }
        else
        {
            count += table[nums[i]];
            table[nums[i]]++;
        }
    }

    free(table);
    
    return count; 
}