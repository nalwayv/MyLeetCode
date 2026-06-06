public class Solution
{
    public int[] LeftRightDifference(int[] nums)
    {
        int rSum = 0;
        for (int i = 1; i < nums.Length; i++)
            rSum += nums[i];

        int lSum = 0;
        int[] result = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++)
        {
            result[i] = int.Abs(lSum - rSum);
            lSum += nums[i];

            if (i + 1 < nums.Length)
                rSum -= nums[i + 1];
        }

        return result;
    }
}

class Program
{
    private static void Main()
    {
        int[] nums = [10, 4, 8, 3];
        Solution solution = new();
        int[] result = solution.LeftRightDifference(nums);

        Console.Write("[");
        foreach (var val in result)
        {
            Console.Write($" {val} ");
        }
        Console.WriteLine("]");
    }
}