public class Solution 
{
    public IList<bool> PrefixesDivBy5(int[] nums) {
        bool[] result = new bool[nums.Length];
        int binaryNumber = 0;
        for(int i = 0; i < nums.Length; i++)
        {
            binaryNumber = binaryNumber * 2 + nums[i];
            binaryNumber %= 100000;

            if (binaryNumber % 5 == 0)
            {
                result[i] = true;
            }
        }
        return result.ToList();
    }
}