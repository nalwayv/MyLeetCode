namespace Leet3318;

using System.Linq;

public class Solution
{
    public int[] FindXSum(int[] nums, int k, int x)
    {
        List<int> result = new List<int>();

        for (int i = 0; i <= nums.Length - k; i++)
        {
            Dictionary<int, int> map = new Dictionary<int, int>();
            for (int j = i; j < i + k; j++)
            {
                map[nums[j]] = map.GetValueOrDefault(nums[j], 0) + 1;
            }

            var frequency = map.OrderByDescending(val => val.Value).ThenByDescending(val => val.Key).ToList();

            int xSum = frequency.Take(x).Sum(item => item.Key * item.Value);
            result.Add(xSum);
        }

        return result.ToArray();
    }
}

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("3318. Find X-Sum of All K-Long Subarrays I");

        Solution solution = new Solution();
        int[] nums = [1, 1, 2, 2, 3, 4, 2, 3];
        var result = solution.FindXSum(nums, 6, 2);
        Console.Write("[");
        foreach (var item in result)
        {
            Console.Write($" {item} ");
        }
        Console.WriteLine("]");
    }
}