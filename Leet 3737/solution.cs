public class Solution 
{
    public int CountMajoritySubarrays(int[] nums, int target) 
    {
        int count = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            int frequency = 0;
            for (int j = i; j < nums.Length; j++)
            {
                if (nums[j] == target)
                {
                    frequency++;
                }

                if (2 * frequency > (j - i + 1))
                {
                    count++;
                }
            }
        }

        return count;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3737. Count Subarrays With Majority Element I");
        Solution solution = new();
        
        int[] nums = [1,2,2,3];
        int majorCount = solution.CountMajoritySubarrays(nums, 2);
        
        Console.WriteLine($"Result: {majorCount}");
    }
}