public class Solution 
{
    public int MinimumCost(int[] cost) 
    {
        // Sort array and take 2 and skip the 3rd.

        Array.Sort(cost);

        int costTotal = 0;
        for (int i = cost.Length - 1; i >= 0; i--)
        {
            // Because we are iterating from the end, 
            // we need to calculate the forward index to determine if it's the 3rd candy.
            int forward_i = cost.Length - i - 1;
            if ((forward_i + 1) % 3 == 0) 
                continue;

            costTotal += cost[i];
        }
        
        return costTotal;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("2144. Minimum Cost of Buying Candies With Discount");

        Solution solution = new();
        int result = solution.MinimumCost([6,5,7,9,2,2]);
        Console.WriteLine($"Min cost = {result}");
    }
}