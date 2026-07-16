public class Solution 
{
    private static int Gcd(int a, int b) 
    {
        return b == 0 ? a : Gcd(b, a % b);
    }

    public static long GcdSum(int[] nums) 
    {
        int[] prefixGcd = new int[nums.Length];
        int mx = nums[0];
        for(int i = 0; i < nums.Length; i++)
        {
            mx = Math.Max(mx, nums[i]);
            prefixGcd[i] = Gcd(mx, nums[i]);
        }
        
        Array.Sort(prefixGcd);

        int lo = 0;
        int hi = nums.Length - 1;
        long result = 0;

        while (lo < hi)
        {
            result += Gcd(prefixGcd[lo], prefixGcd[hi]);

            lo++;
            hi--;
        }

        return result;
    }
}


class Program
{
    static void TestCase(int[] nums, int expected)
    {
        long sum = Solution.GcdSum(nums);
        string result = sum == expected ? "Pass" : "Fail";
        Console.WriteLine($"Result: {result}");
    }

    static void Main()
    {
        Console.WriteLine("3867. Sum of GCD of Formed Pairs");

        int[] nums = [2,6,4];
        TestCase(nums, 2);
    }
}