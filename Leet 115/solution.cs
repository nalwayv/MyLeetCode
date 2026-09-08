class Solution
{
    /// <summary>
    /// Given two strings s and t, return the number of distinct subsequences of s which equals t.
    /// </summary>
    /// <param name="s"></param>
    /// <param name="t"></param>
    /// <returns></returns>
    public static int NumDistinct(string s, string t)
    {
        int[,] dp = new int[t.Length + 1, s.Length + 1];

        for (int i = 0; i < dp.GetLength(1); i++)
        {
            dp[0, i] = 1;
        }

        for (int i = 1; i < dp.GetLength(0); i++)
        {
            for (int j = 1; j < dp.GetLength(1); j++)
            {
                var topLeft = (s[j - 1] == t[i - 1]) ? dp[i - 1, j - 1] : 0;
                var left = dp[i, j - 1];

                dp[i, j] = left + topLeft;
            }
        }

        return dp[t.Length, s.Length];
    }
}


class Program
{
    private static void Main()
    {
        Console.WriteLine("115. Distinct Subsequences");

        int result = Solution.NumDistinct("rabbbit", "rabbit");
        Console.WriteLine($"Result: {result}");
    }
}