namespace Leet
{
    public class Solution 
    {
        public int[] MinBitwiseArray(IList<int> nums) 
        {
            int[] ans = new int[nums.Count];
            for(int i = 0; i < nums.Count; i++)
            {            
                ans[i] = -1;
                if (nums[i] % 2 != 0)
                {
                    int numPlus = nums[i] + 1;
                    ans[i] = nums[i] - (numPlus & -numPlus) / 2;
                }
            }
            return ans;
        }
    }
    
    class Program
    {
        static void Main()
        {
            Console.WriteLine("3315. Construct the Minimum Bitwise Array II");

            Solution solution = new();
            
            int[] case1Result = solution.MinBitwiseArray([2, 3, 5, 7]);
            Console.Write("[ 2 3 5 7 ] should equal [ -1 1 4 3 ] ? [");
            foreach(int val in case1Result)
            {
                Console.Write($" {val} ");
            }
            Console.WriteLine("]");
        }
    }
}