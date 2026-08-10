class Solution
{
    /// <summary>
    /// Check if Alice can win the stone game against Bob if both players play optimally.
    /// On each turn a player can remove any non zero square number of stones from the pile
    /// </summary>
    /// <param name="n">number of stones in the pile</param>
    /// <returns>true if Alice can win the game</returns>
    public bool WinnerSquareGame(int n)
    {
        bool[] dp = new bool[n + 1];
        for (int i = 1; i <= n; i++)
        {
            int j = 1;

            // iterate through square numbers up to i and check if dp[i - j * j] is false
            // if it is, set dp[i] to true and break the loop
            while (j * j <= i)
            {
                if (!dp[i - j * j])
                {
                    dp[i] = true;
                    break;
                }

                j++;
            }
        }

        return dp[n];
    }
}

class Program
{

    private static void TestCase(Solution solution, int n, bool expected)
    {
        var testResult = solution.WinnerSquareGame(n) == expected ? "Pass" : "Fail";
        Console.WriteLine($"Test Reault {n} should equal {expected}: {testResult}");
    }

    private static void Main()
    {
        Console.WriteLine("1510. Stone Game IV");

        Solution solution = new();

        TestCase(solution, 1, true);
        TestCase(solution, 2, false);
        TestCase(solution, 4, true);
    }
}