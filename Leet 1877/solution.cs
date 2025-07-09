public class Solution
{
    public int MinPairSum(int[] nums)
    {
        Array.Sort(nums);

        int result = -1;
        for (int i = 0; i < nums.Length / 2; i++)
        {
            result = int.Max(result, nums[i] + nums[nums.Length - i - 1]);
        }
        return result;
    }
}