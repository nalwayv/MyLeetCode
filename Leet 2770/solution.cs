public class Solution 
{
    public int MaximumJumps(int[] nums, int target) 
    {
        int[] dp = new int[nums.Length];
        Array.Fill(dp, -1);
        dp[0] = 0;


        for(int i = 0; i < nums.Length; i++)
        {
            if(dp[i] == -1)
                continue;

            for(int j = i + 1; j < nums.Length; j++)
            {
                var diff = nums[j] - nums[i];
                if(-target <= diff && diff <= target)
                {
                    dp[j] = int.Max(dp[j], dp[i] + 1);
                }
            }
        }

        return dp[^1];
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("2770. Maximum Number of Jumps to Reach the Last Index");

        Solution solution = new();

        int[] nums = [1,3,6,4,1,2];
        int target = 2;
        string result = solution.MaximumJumps(nums, target) == 3 ? "Pass":"Fail";
        Console.WriteLine($"case 1 should equal 3? {result}");
    }
}

