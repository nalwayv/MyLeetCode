public class Solution
{
    public int LongestSubsequence(int[] nums)
    {
        int allZero = 0;
        int xsum = 0;
        foreach(int num in nums)
        {
            if (num == 0)
            {
                allZero++;
            }
            xsum ^= num;
        }

        if (allZero == nums.Length)
        {
            return 0;
        }

        if (xsum == 0)
        {
            return nums.Length - 1;
        }

        return nums.Length;
    }
}
