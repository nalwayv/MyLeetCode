
public class Solution
{
    public int[] SeparateDigits(int[] nums)
    {
        List<int> result = [];
        foreach (int num in nums)
        {
            if (num <= 9)
            {
                result.Add(num);
            }
            else
            {
                foreach (var value in num.ToString())
                {
                    result.Add(value - '0');
                }
            }
        }

        return result.ToArray();
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("2553. Separate the Digits in an Array");
        Solution solution = new();

        int[] nums = [13, 25, 83, 77];
        int[] result = solution.SeparateDigits(nums);

        Console.WriteLine("Input: [ 13 25 83 77 ]");
        Console.Write("Output: [");
        foreach (int r in result)
        {
            Console.Write($" {r} ");
        }
        Console.WriteLine("]");
    }
}