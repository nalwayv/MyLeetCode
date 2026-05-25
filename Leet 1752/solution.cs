public class Solution
{
    public bool Check(int[] nums)
    {
        int count = 0;

        if (nums[0] < nums[^1])
            count++;

        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i - 1] > nums[i])
                count++;

            if (count > 1)
                return false;
        }

        return true;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("1752. Check if Array Is Sorted and Rotated");

        Solution solution = new();

        int[] nums = [3, 4, 5, 1, 2];
        string result = solution.Check(nums) ? "Pass" : "Fail";
        Console.WriteLine($"Check [ 3 4 5 1 2] should pass? {result}");
    }
}