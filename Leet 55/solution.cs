public class Solution
{
    public bool CanJump(int[] nums)
    {
        int last = nums.Length - 1;
        for (int i = nums.Length - 1; i >= 0; i--)
        {
            if (i + nums[i] >= last)
                last = i;
        }
        return last == 0;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("55. Jump Game");

        int[] nums = [2, 3, 1, 1, 4];
        
        Solution solution = new();
        string result = solution.CanJump(nums) ? "Pass" : "Fail";
        Console.WriteLine($"Can Jump should pass ? {result}");
    }
}