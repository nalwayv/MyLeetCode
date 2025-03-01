using System;

public class Solution 
{
    public int[] ApplyOperations(int[] nums) 
    {
        /*
         NOTE:
         You are given a 0-indexed array nums of size n consisting of non-negative integers
         You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums
        
         If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
         After performing all the operations, shift all the 0's to the end of the array
        
         For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
         Return the resulting array
         
         Note that the operations are applied sequentially, not all at once.
        */

		// Apply pattern
        for(int i = 1; i < nums.Length; i++)
		{
			if(nums[i-1] == nums[i])
			{
				nums[i-1] = nums[i-1] * 2;
				nums[i] = 0;
			}
		}
		
		// Move zeros to end
		int j = 0;
		for(int i = 0; i < nums.Length; i++)
		{
			if(nums[i] != 0)
			{
				int tmp = nums[j];
				nums[j] = nums[i];
				nums[i] = tmp;
				j += 1;
			}
		}
		
		return nums;
    }
}


public class Program
{
	public static void Main()
	{
		Console.WriteLine("2460. Apply Operations to an Array");


		Solution sol = new();
		int[] nums = [1,2,2,1,1,0];
		nums = sol.ApplyOperations(nums);

		Console.Write("[");
		foreach(var num in nums)
		{
			Console.Write($" {num} ");
		}
		Console.WriteLine("]");
	}
}