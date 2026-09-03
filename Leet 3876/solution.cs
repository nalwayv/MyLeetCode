class Solution
{
    public bool UniformArray(int[] nums1)
    {
        int minOdd = -1;
        foreach(int num in nums1)
        {
            if (num % 2 == 1)
            {
                if (minOdd == -1 || num < minOdd)
                {
                    minOdd = num;
                }
            }
        }

        // Rules
        // even - odd = odd
        // nums[i] - nums[j] should be >= 1
        foreach(int num in nums1)
        {
            if (num % 2 == 0 && num - minOdd < 1)
            {
                return false;
            }
        }

        return true;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3876. Construct Uniform Parity Array II");

        var solution = new Solution();

        int[] nums1 = [1,4,7];
        string result = solution.UniformArray(nums1) ? "pass":"fail";
        Console.WriteLine($"[1,4,7] should equal true? {result}");
    }
}