public class Solution 
{
    private bool Check(int[] position, int m, int distance)
    {
        int count = 1;
        int prev = position[0];
        for (int i = 1; i < position.Length; i++)
        {
            int curr = position[i];
            if (curr - prev >= distance)
            {
                count += 1;
                prev = curr;
                if (count == m)
                {
                    return true;
                }
            }
        }

        return false;
    }

    public int MaxDistance(int[] position, int m) 
    {
        Array.Sort(position);

        int result = 0;
        int lo = 1;
        int hi = position[position.Length - 1] - lo;

        while (lo <= hi)
        {
            int mid = (lo + hi) / 2;
            if (Check(position, m, mid))
            {
                result = mid;
                lo = mid + 1;
            }
            else
            {
                hi = mid - 1;
            }
        }

        return result;
    }
}


internal class Program
{
    private static void Main()
    {
        Console.WriteLine("1552. Magnetic Force Between Two Balls");
        Solution solution = new();
        int[] positions = [1, 2, 3, 4, 7];
        int m = 3;
        int result = solution.MaxDistance(positions, m);

        Console.WriteLine($"Case 1 should equal 3? {result}");
    }
}