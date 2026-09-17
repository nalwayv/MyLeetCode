using System.Numerics;

Console.WriteLine("1621. Number of Sets of K Non-Overlapping Line Segments");

Console.WriteLine(Solution.NumberOfSets(30, 7) == 796297179);
Console.WriteLine(Solution.NumberOfSets(42, 25) == 630775896);

class Solution
{
    /// <summary>
    /// combination function
    /// </summary>
    private static BigInteger Comb(long n, long k)
    {
        if (n < 0 || k < 0 || k > n)
        {
            return 0;
        }

        k = Math.Min(k, n - k);
        
        BigInteger result = 1;
        for(long i = 1; i <= k; i++)
        {
            result = result * (n - k + i) / i;
        }
        return result;
    }

    public static int NumberOfSets(int n, int k)
    {
        return (int)(Comb(n + k - 1, 2 * k) % 1000000007);
    }
}