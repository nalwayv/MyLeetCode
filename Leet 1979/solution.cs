namespace Leet
{
    class Solution
    {
        /// <summary>
        /// Return the Greatest Common Devisor between ints a and b recursivly.
        /// </summary>
        /// <returns>gcd between a and b</returns>
        private static int Gcd(int a, int b) =>
            b == 0 ? a : Gcd(b, a % b);

        /// <summary>
        /// Return the Greatest Common Devisor of the smallest and largest number from nums.
        /// </summary>
        /// <param name="nums">array of ints</param>
        /// <returns>GCD of smallest and largest number from nums</returns>
        public static int FindGcd(int[] nums)
        {
            int mx = nums[0];
            int mn = nums[0];

            foreach (int num in nums)
            {
                mx = Math.Max(mx, num);
                mn = Math.Min(mn, num);
            }

            return Gcd(mx, mn);
        }
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("1979. Find Greatest Common Divisor of Array");

        int[] nums = [2, 5, 6, 9, 10];
        string result = Leet.Solution.FindGcd(nums) == 2 ? "Pass" : "Fail";
        Console.WriteLine($"Case1 should equal 2? {result}");
    }
}