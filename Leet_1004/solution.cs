using System.Text;

namespace Leet1004;

public class Solution
{
    public int LongestOnes(int[] nums, int k)
    {
        int length = 0;
        int zeroCount = 0;

        int p2 = 0;
        for (int p1 = 0; p1 < nums.Length; p1++)
        {
            if (nums[p1] == 0)
            {
                zeroCount++;
            }

            while (zeroCount > k)
            {
                if (nums[p2] == 0)
                {
                    zeroCount--;
                }
                p2++;
            }

            length = Math.Max(length, p1 - p2 + 1);
        }

        return length;
    }
}

static class Program
{
    static void Main()
    {
        Console.WriteLine("1004. Max Consecutive Ones III");

        Console.WriteLine("_____ Case 1 _____");
        int[] nums = { 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0 };
        int k = 2;
        int result = new Solution().LongestOnes(nums, k);
        Console.WriteLine("Result: {0}", result);
    }
}