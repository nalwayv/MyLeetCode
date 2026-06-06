namespace Leet
{
    public class Solution
    {
        public int MinMirrorPairDistance(int[] nums)
        {
            Dictionary<int, int> distances = [];

            var minDist = int.MaxValue;
            for (int i = 0; i < nums.Length; i++)
            {
                int num = nums[i];

                // get reverse of num
                int reverse = 0;
                while (num > 0)
                {
                    var tmp = num % 10;
                    reverse = reverse * 10 + tmp;
                    num /= 10;
                }

                // reset num
                num = nums[i];

                // if reverse of num is in dictionary then update mindist
                if (distances.TryGetValue(num, out int idx))
                    minDist = int.Min(minDist, int.Abs(i - idx));

                // add reverse and current index to dictionary
                distances[reverse] = i;
            }

            // return min dist or -1 if non is found
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

        int testCase1 = solution.MinMirrorPairDistance([12, 21, 45, 33, 54]);
        Console.WriteLine($"Test Case 1: {testCase1}");

        int testCase2 = solution.MinMirrorPairDistance([120, 21]);
        Console.WriteLine($"Test Case 2: {testCase2}");

        int testCase3 = solution.MinMirrorPairDistance([21, 120]);
        Console.WriteLine($"Test Case 3: {testCase3}");
    }
}