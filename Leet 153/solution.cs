public class Solution
{
    public int FindMin(int[] nums)
    {
        int result = nums[0];
        for(int i = 0; i < nums.Length - 1; i++)
        {
            if (nums[i + 1] - nums[i] < 0)
            {
                result = int.Min(result, nums[i + 1]);
            }
        }
        return result;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("153. Find Minimum in Rotated Sorted Array");
        Solution solution = new();

        Console.WriteLine(solution.FindMin([3, 4, 5, 1, 2]) == 1);
        Console.WriteLine(solution.FindMin([4, 5, 6, 7, 0, 1, 2]) == 0);
        Console.WriteLine(solution.FindMin([11, 13, 15, 17]) == 11);
        Console.WriteLine(solution.FindMin([2, 3, 4, 5, 1]) == 1);
    }
}