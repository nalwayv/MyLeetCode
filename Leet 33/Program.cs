public class Solution 
{
    private int BinarySearch(int[] nums, int target)
    {
        int lo = 0;
        int hi = nums.Length - 1;

        while (lo <= hi)
        {
            int mi = (lo + hi) / 2;
            if (nums[mi] == target)
            {
                return mi;
            }

            if (nums[mi] < target)
            {
                lo = mi + 1;
            }
            else
            {
                hi = mi - 1;
            }
        }

        return -1;
    }

    private int GetMinIdx(int[] nums)
    {
        int min = int.MaxValue;
        int idx = -1;

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] < min)
            {
                min = nums[i];
                idx = i;
            }
        }

        return idx;
    }

    // private void PrintArray(int[] nums)
    // {
    //     Console.Write("[");
    //     foreach(int i in nums)
    //     {
    //         Console.Write($" {i} ");
    //     }
    //     Console.WriteLine("]");
    // }

    public int Search(int[] nums, int target) 
    {
        int n = nums.Length;
        int lo = GetMinIdx(nums);

        // tmp rotate array starting from lo
        int[] tmp = new int[n];
        int j = lo;
        for (int i = 0; i < n; i++)
        {
            tmp[i] = nums[j];
            j = (j + 1) % n;
        }

        int idx = BinarySearch(tmp, target);
        if (idx != -1)
        {
            return (lo + idx) % n;
        }

        return -1;
    }
}


internal class Program
{
    private static void Main()
    {
        Console.WriteLine("33. Search in Rotated Sorted Array");
        Solution solution = new();
    
        Console.WriteLine("nums = [4,5,6,7,0,1,2], target = 0");
        int result1 = solution.Search([4,5,6,7,0,1,2], 0);
        Console.WriteLine(result1);

        Console.WriteLine("nums = [4,5,6,7,0,1,2], target = 3");
        int result2 = solution.Search([4,5,6,7,0,1,2], 3);
        Console.WriteLine(result2);

        Console.WriteLine("nums = [1], target = 0");
        int result3 = solution.Search([1], 0);
        Console.WriteLine(result3);

        Console.WriteLine("nums = [5,6,7,8,9,1,2,3,4], target = 2");
        int result4 = solution.Search([5,6,7,8,9,1,2,3,4], 2);
        Console.WriteLine(result4);
    }
}