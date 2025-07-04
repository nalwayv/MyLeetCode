public class Solution
{
    private int BisectLeft(int[] nums, int target)
    {
        int lo = 0;
        int hi = nums.Length;

        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] < target)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        return lo;
    }

    private int BisectRight(int[] nums, int target)
    {
        int lo = 0;
        int hi = nums.Length;

        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (target < nums[mid])
            {
                hi = mid;
            }
            else
            {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private int GetLeftMostIdx(int[] nums, int target)
    {
        int idx = BisectLeft(nums, target);
        if (idx != nums.Length && nums[idx] == target)
        {
            return idx;
        }
        return -1;
    }

    private int GetRightMostIdx(int[] nums, int target)
    {
        int idx = BisectRight(nums, target);
        if (idx != 0 && nums[idx - 1] == target)
        {
            return idx - 1;
        }
        return -1;
    }

    public int[] SearchRange(int[] nums, int target)
    {
        int[] result = [-1, -1];
        
        result[0] = GetLeftMostIdx(nums, target);
        if (result[0] == -1)
        {
            return result;
        }

        result[1] = GetRightMostIdx(nums, target);
        return result;
    }
}

internal class Program
{
    private static void PrintArr(int[] arr)
    {
        Console.Write("[");
        foreach (int num in arr)
        {
            Console.Write($" {num} ");
        }
        Console.WriteLine("]");
    }

    private static void Main()
    {
        Console.WriteLine("34. Find First and Last Position of Element in Sorted Array");
        Solution solution = new();
        //            0  1  2  3  4  05
        int[] nums = [5, 7, 7, 8, 8, 10];
        int target = 8;

        int[] result = solution.SearchRange(nums, target);
        PrintArr(result);
    }
}