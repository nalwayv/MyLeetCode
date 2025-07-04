public class Solution
{
    private bool IsBadVersion(int b)
    {
        // NOTE: Leet Api
        // The isBadVersion API is already defined for you.
        return false;
    }

    public int FirstBadVersion(int n)
    {
        int low = 1;
        int high = n;
        while (low < high)
        {
            int mid = low + (high - low) / 2;
            if (!IsBadVersion(mid))
            {
                low = mid + 1;
            }
            else
            {
                high = mid;
            }
        }

        return low;
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("278. First Bad Version");
        Solution solution = new();
        int version = solution.FirstBadVersion(10);
        Console.WriteLine($"First Bad Version: {version}");
    }
}