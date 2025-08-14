public class Solution
{
    public int NumberOfWays(int n, int x)
    {
        List<int> nums = [];
        for (var i = 1; i <= n; i++)
        {
            var pow = (int)Math.Pow(i, x);
            if (pow <= n)
            {
                nums.Add(pow);
            }
        }

        var dp = new int[n + 1];
        dp[0] = 1;
        var mod = (int)(1e9 + 7);

        foreach (var num in nums)
        {
            for (var i = n; i >= num; i--)
            {
                dp[i] = (dp[i] + dp[i - num]) % mod;
            }
        }

        return dp[n];
    }
}


internal static class Program
{
    private static void Main()
    {
        Console.WriteLine("2787. Ways to Express an Integer as Sum of Powers");

        Solution sol = new();

        int case1 = sol.NumberOfWays(10, 2);
        Console.WriteLine($"Case1 (n=10, x=2) should equal 1? {case1}");
        
        int case2 = sol.NumberOfWays(226, 1);
        Console.WriteLine($"Case1 (n=226, x=1) should equal 239229946? {case2}");
    }
}