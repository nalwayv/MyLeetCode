public class Solution
{
    public int MaximumElementAfterDecrementingAndRearranging(int[] arr)
    {
        // RULES:
        // The value of the first element in arr must be 1.
        // The absolute difference between any 2 adjacent elements must be less than or equal to 1

        int[] arrCopy = new int[arr.Length];
        Array.Copy(arr, arrCopy, arr.Length);

        Array.Sort(arrCopy);

        // first value has to be 1 thats the rule.
        arrCopy[0] = 1;

        int maxValue = 1;
        for (int i = 1; i < arrCopy.Length; i++)
        {
            // if out of range set to previous + 1
            if (Math.Abs(arrCopy[i] - arrCopy[i - 1]) > 1)
            {
                arrCopy[i] = arrCopy[i - 1] + 1;
            }

            maxValue = Math.Max(maxValue, arrCopy[i]);
        }

        return maxValue;
    }
}


class Program
{
    private static void Main()
    {
        Console.WriteLine("1846. Maximum Element After Decreasing and Rearranging");

        Solution solution = new();

        int[] nums = [2, 2, 1, 2, 1];
        int result = solution.MaximumElementAfterDecrementingAndRearranging(nums);
        Console.WriteLine($"Result: {result}");
    }
}