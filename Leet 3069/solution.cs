public class Solution
{
    public int[] ResultArray(int[] nums)
    {
        var a = new List<int>();
        var b = new List<int>();

        a.Add(nums[0]);
        b.Add(nums[1]);

        for (int i = 2; i < nums.Length; i++)
        {
            if (a[^1] > b[^1])
            {
                a.Add(nums[i]);
            }
            else
            {
                b.Add(nums[i]);
            }
        }

        a.AddRange(b);

        return [.. a];
    }
}


class Program
{
    private static void Main()
    {
        Console.WriteLine("3069. Distribute Elements Into Two Arrays I");

        Solution solution = new();
        int[] result = solution.ResultArray([5, 4, 3, 8]);

        Console.Write("[");
        foreach (int r in result)
        {
            Console.Write($" {r} ");
        }
        Console.WriteLine("]");
    }
}