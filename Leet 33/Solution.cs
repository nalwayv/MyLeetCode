public class Solution 
{
    public int Search(int[] nums, int target) 
    {
        int lo = 0;
        int hi = nums.Length - 1;
        
        while (lo <= hi) 
        {
            int mid = lo + (hi - lo) / 2;
            
            if (nums[mid] == target) 
                return mid;

            if (nums[mid] >= nums[lo]) 
            {
                if (target >= nums[lo] && target < nums[mid])
                    hi = mid - 1;
                else
                    lo = mid + 1;
            } 
            else 
            {
                if (target > nums[mid] && target <= nums[hi])
                    lo = mid + 1;
                else
                    hi = mid - 1;
            }
        }

        return -1;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("33. Search in Rotated Sorted Array");
        int[] nums = [4,5,6,7,0,1,2];
        int target = 0;

        Solution solution = new();
        int idx = solution.Search(nums, target);
        Console.WriteLine("Search for idx 0 in rotated array [4,5,6,7,0,1,2]");
        
        if (idx != -1)
            Console.WriteLine($"Found at index: {idx}");
        else
            Console.WriteLine($"Not Found");
    }
}