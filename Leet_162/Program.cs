public class Solution 
{
    public int FindPeakElement(int[] nums) 
    {
        // Binary Search Template II
        if (nums.Length == 0)
        {
            return -1;
        }

        int lo = 0;
        int hi = nums.Length - 1;

        while (lo < hi)
        {
            int mi = lo + (hi-lo) / 2;
            
            if (nums[mi] == nums[mi + 1])
            {
                return -1;
            }

            if (nums[mi] < nums[mi + 1])
            {
                lo = mi + 1;
            }
            else
            {
                hi = mi;
            }
        }

        return lo;
    }
}

internal class Program
{
    private static void Example1(Solution sol)
    {
        int idx = sol.FindPeakElement([1,2,3,1]);
        Console.WriteLine(idx == 2);
    }

    private static void Example2(Solution sol)
    {
        int idx = sol.FindPeakElement([1,2,1,3,5,6,4]);
        Console.WriteLine(idx == 5);
    }

    private static void Main()
    {
        Console.WriteLine("162. Find Peak Element");
        Solution solution = new();

        Example1(solution);
        Example2(solution);
    }
}