public class Solution 
{
    public long ColoredCells(int n) 
    {
        long result = 1;
        long p1 = 0;
        long p2 = 0;

        for(int i = 1; i <= n; i++)
        {
            p1 = 4 * i;
            result += p2;
            p2 = p1;
        }

        return result;
    }
}

public class Program
{
    public static void Main()
    {
        Console.WriteLine("2579. Count Total Number of Colored Cells");

        Solution solution = new();

        long[] results = [1,5,13,25,41];
        for(int i = 1; i <= results.Length; i++)
        {
            if(solution.ColoredCells(i) == results[i-1])
                Console.WriteLine($"Case {i}: pass");
            else
                Console.WriteLine($"Case {i}: fail");
        }
    }
}