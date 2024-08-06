public class Solution
{
    public int FindMin(int[] nums)
    {
        int lo = 0;
        int hi = nums.Length - 1;
        int min = int.MaxValue;

        while (lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;

            if (nums[mid] > nums[hi])
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid - 1;
            }

            min = int.Min(min, nums[mid]);
        }

        return min;
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("153. Find Minimum in Rotated Sorted Array");
        Solution solution = new();

        Console.WriteLine(solution.FindMin([3, 4, 5, 1, 2]) == 1);
        Console.WriteLine(solution.FindMin([4, 5, 6, 7, 0, 1, 2]) == 0);
        Console.WriteLine(solution.FindMin([11, 13, 15, 17]) == 11);
        Console.WriteLine(solution.FindMin([2, 3, 4, 5, 1]) == 1);
    }
}