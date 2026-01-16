
namespace Leet
{
    public class Solution
    {
        public int GarbageCollection(string[] garbage, int[] travel) 
        {
            for(int i = 1; i < travel.Length; i++)
            {
                travel[i] += travel[i-1];
            }

            int totalTime = 0;
            int paperLastStop = -1;
            int glassLastStop = -1;
            int metalLastStop = -1;

            for (int i = 0; i < garbage.Length; i++)
            {
                totalTime += garbage[i].Length;

                if (garbage[i].Contains('P'))
                {
                    paperLastStop = i;
                }

                if (garbage[i].Contains('G'))
                {
                    glassLastStop = i;
                }

                if (garbage[i].Contains('M'))
                {
                    metalLastStop = i;
                }
            }

            if (paperLastStop > 0)
            {
                totalTime += travel[paperLastStop - 1];
            }

            if (glassLastStop > 0)
            {
                totalTime += travel[glassLastStop - 1];
            }

            if (metalLastStop > 0)
            {
                totalTime += travel[metalLastStop - 1];
            }

            return totalTime;
        }
    }
    
    class Program
    {
        private static void TestCase(Solution solution, string[] garbage, int[] travel, int expected)
        {
            string result = solution.GarbageCollection(garbage, travel) == expected ? "pass" : "fail";
            var toStr = string.Concat(garbage);

            Console.WriteLine($"{toStr} should equal {expected}: {result}");
        }

        private static void Main()
        {
            Console.WriteLine("2391. Minimum Amount of Time to Collect Garbage");

            Solution solution = new();
            TestCase(solution, ["G","P","GP","GG"], [2,4,3], 21);
            TestCase(solution, ["MMM","PGM","GP"], [3,10], 37);
            TestCase(solution, ["G","M"], [1], 3);
        }
    }
}