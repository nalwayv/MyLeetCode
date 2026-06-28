public class Solution
{
    public int MaximumLength(int[] nums)
    {
        Dictionary<long, int> frequency = [];
        foreach(int num in nums)
        {
            frequency.TryGetValue(num, out int val);
            frequency[num] = val + 1;
        }

        frequency.TryGetValue(1, out int result);
        if (result > 0)
        {
            frequency[1] = 0;
        }

        if (result % 2 == 0)
        {
            result--;
        }

        foreach(var key in frequency.Keys)
        {
            int count = 0;
            long curr = key;

            while (frequency.TryGetValue(curr, out int val) && val > 1)
            {
                count += 2;
                curr *= curr;
            }
            
            int add = frequency.ContainsKey(curr) ? 1 : -1;
            result = Math.Max(result, count + add);
        }

        return result;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3020. Find the Maximum Number of Elements in Subset");

        Solution solution = new();

        int[] nums1 = [5,4,1,2,2];
        Console.WriteLine($"Result: {solution.MaximumLength(nums1)}");
        
        int[] nums2 = [1,3,2,4];
        Console.WriteLine($"Result: {solution.MaximumLength(nums2)}");

    }
}