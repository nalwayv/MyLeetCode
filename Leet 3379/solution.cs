public class Solution 
{
    private int Wrapi(int value, int lo, int hi)
    {
        return lo + ((value - lo) % (hi - lo) + (hi - lo)) % (hi - lo);
    }

    public int[] ConstructTransformedArray(int[] nums) 
    {
        int[] result = new int[nums.Length];
        for(int i = 0; i < nums.Length; i++)
        {
            result[i] = nums[Wrapi(i + nums[i], 0, nums.Length)];
        }
        return result;
    }
}

class Program
{
    static void PrintArray(int[] nums)
    { 
        Console.WriteLine($"[{string.Join(", ", nums)}]");
    }

    static void Main()
    {
        Console.WriteLine("3379. Transformed Array");
        Solution solution = new();
        int[] case1 = solution.ConstructTransformedArray([3,-2,1,1]);
        PrintArray(case1);
    }
}