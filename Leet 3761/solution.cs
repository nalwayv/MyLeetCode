using System.Text;

namespace Leet 
{
    public class Solution 
    {
        private static string RevserseString(string value)
        {
            StringBuilder sb = new();
            foreach(var val in value)
                sb.Insert(0, val);

            // remove any leading zero's
            while(sb.Length > 0 && sb[0] == '0')
                sb.Remove(0, 1);

            return sb.ToString();
        }

        public int MinMirrorPairDistance(int[] nums) 
        {
            Dictionary<string, int> map = [];

            var minDist = int.MaxValue;
            for(int i = 0; i < nums.Length; i++)
            {
                string strNum = nums[i].ToString();
                string revNum = RevserseString(strNum);

                if (map.ContainsKey(strNum))
                    minDist = int.Min(minDist, int.Abs(i - map[strNum]));
                
                map[revNum] = i;
            }

            return minDist == int.MaxValue ? -1 : minDist;
        }
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3761. Minimum Absolute Distance Between Mirror Pairs");

        Leet.Solution solution = new();

        int testCase1 = solution.MinMirrorPairDistance([12,21,45,33,54]);
        Console.WriteLine($"Test Case 1: {testCase1}");

        int testCase2 = solution.MinMirrorPairDistance([120,21]);
        Console.WriteLine($"Test Case 2: {testCase2}");

        int testCase3 = solution.MinMirrorPairDistance([21,120]);
        Console.WriteLine($"Test Case 3: {testCase3}");
    }
}