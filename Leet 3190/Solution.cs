public class Solution
{
    public int MinimumOperations(int[] nums)
    {
        int count = 0;
        int[] ones = [-1, 1];

        foreach (int num in nums)
        {
            foreach (int one in ones)
            {
                if ((num + one) % 3 == 0)
                {
                    count++;
                }
            }
        }

        return count;
    }
}