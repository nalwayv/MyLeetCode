Console.WriteLine("3871. Count Commas in Range II");

long number = 1234567;
Console.WriteLine($"Result for {number} = {Solution.CountCommas(number)}");

class Solution
{
    public static long CountCommas(long n)
    {
        long total = 0;
        // comma's
        // 1,000            -> 1
        // 1,000,000        -> 2
        // 1,000,000,000    -> 3
        long commaThreshold = 1000;
        while (commaThreshold <= n)
        {
            total += n - commaThreshold + 1;

            // move to next comma threshold
            commaThreshold *= 1000;
        }
        return total;
    }
}

