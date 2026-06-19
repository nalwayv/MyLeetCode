public class Solution
{
    public int LargestAltitude(int[] gain)
    {
        int sum = 0;
        int height = 0;

        foreach (int g in gain)
        {
            sum += g;
            height = int.Max(height, sum);
        }

        return height;
    }
}

class Program
{
    private static void Main()
    {
        Solution solution = new();

        int[] gains1 = [-5, 1, 5, 0, -7];
        int[] gains2 = [-4, -3, -2, -1, 4, 3, 2];
        int[] gains3 = [52, -91, 72];

        int result1 = solution.LargestAltitude(gains1);
        int result2 = solution.LargestAltitude(gains2);
        int result3 = solution.LargestAltitude(gains3);

        string expected1 = result1 == 1 ? "Pass" : "Fail";
        string expected2 = result2 == 0 ? "Pass" : "Fail";
        string expected3 = result3 == 52 ? "Pass" : "Fail";

        Console.WriteLine($"Result1 should equal 1 ? {expected1}");
        Console.WriteLine($"Result2 should equal 0 ? {expected2}");
        Console.WriteLine($"Result3 should equal 52 ? {expected3}");
    }
}