public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int lo = 0;
        int hi = nums.Length - 1;

        while (lo <= hi)
        {
            int m = (lo + hi) / 2;

            if (nums[m] == target)
            {
                return m;
            }

            if (nums[m] > target) 
            { 
                hi = m - 1; 
            }
            else
            {
                lo = m + 1;
            }
        }

        return lo;
    }
}

internal class Program
{
    private static void Example1(Solution sol)
    {
        int[] ex1Arr = [1,3,5,6];
        Console.WriteLine($"([1,3,5,6], 5) = {sol.SearchInsert(ex1Arr, 5)}");
    }

    private static void Example2(Solution sol)
    {
        int[] ex1Arr = [1,3,5,6];
        Console.WriteLine($"([1,3,5,6], 2) = {sol.SearchInsert(ex1Arr, 2)}");
    }

    private static void Example3(Solution sol)
    {
        int[] ex1Arr = [1,3,5,6];
        Console.WriteLine($"([1,3,5,6], 7) = {sol.SearchInsert(ex1Arr, 7)}");
    }


    private static void Example4(Solution sol)
    {
        int[] ex1Arr = [1,3,5,6];
        Console.WriteLine($"([1,3,5,6], 4) = {sol.SearchInsert(ex1Arr, 4)}");
    }

    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 35. Search Insert Position");
        Solution solution = new();
        Example1(solution);
        Example2(solution);
        Example3(solution);
        Example4(solution);
    }
}