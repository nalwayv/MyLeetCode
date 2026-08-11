class Solution
{
    public int MissingInteger(int[] nums)
    {
        if (nums.Length == 0)
        {
            return 0;
        }

        int i = 1;
        int pre = nums[0];
        while(i < nums.Length && nums[i] - nums[i-1] == 1)
        {
            pre += nums[i++];
        }

        var present = new HashSet<int>(nums);
        while (present.Contains(pre))
        {
            pre++;
        }
        return pre;
    }
}


class Program
{
    private static void TestCase(Solution solution, int[] nums, int expected)
    {
        string result = solution.MissingInteger(nums) == expected ? "Pass":"Fail";
        Console.WriteLine($"Test case should equal expected: {result}");
    }

    private static void Main()
    {    
        Console.WriteLine("2996. Smallest Missing Integer Greater Than Sequential Prefix Sum");
        
        Solution solution = new();

        int[] nums1 = [1, 2, 3, 2, 5];
        TestCase(solution, nums1, 6);

        int[] nums2 = [3, 4, 5, 1, 12, 14, 13];
        TestCase(solution, nums2, 15);
    }
}