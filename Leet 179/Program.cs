using System.Text;

namespace Leet_179
{
    public class Solution
    {
        private int Comparison(int a, int b)
        {
            string ab = a.ToString() + b.ToString();
            string ba = b.ToString() + a.ToString();
            // Console.WriteLine($"{ab} > {ba}");
            return ab.CompareTo(ba);
        }

        public string LargestNumber(int[] nums)
        {
            Array.Sort(nums, Comparison);
            if (nums[^1] == 0)
            {
                return "0";
            }

            StringBuilder sb = new();
            for (int i = nums.Length - 1; i >= 0; i--)
            {
                sb.Append(nums[i]);
            }
            return sb.ToString();
        }
    }

    internal class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("179. Largest Number");

            Solution sol = new();

            int[] case1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
            Console.WriteLine($"case1 = {sol.LargestNumber(case1)}");

            int[] case2 = [3, 30, 34, 5, 9];
            Console.WriteLine($"case2 = {sol.LargestNumber(case2)}");
        }
    }
}