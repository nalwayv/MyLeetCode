namespace Solution
{
    public class Solution
    {
        public bool CheckPowersOfThree(int n)
        {
            List<double> powers = [];
            int i = 0;
            double current = 0;
            while (current <= n)
            {
                current = Math.Pow(3, i++);
                powers.Add(current);
            }

            double sum = 0;
            for (int j = powers.Count - 1; j >= 0; j--)
            {
                double currentPower = powers[j];
                if (sum + currentPower <= n)
                {
                    sum += currentPower;
                }
            }

            return sum == n;
        }
    }

    public static class TestCases
    {
        public static void Test1(Solution solution)
        {
            string result = solution.CheckPowersOfThree(12) ? "pass" : "fail";
            Console.WriteLine($"Case 1: {result}");
        }

        public static void Test2(Solution solution)
        {
            string result = solution.CheckPowersOfThree(91) ? "pass" : "fail";
            Console.WriteLine($"Case 2: {result}");
        }

        public static void Test3(Solution solution)
        {
            string result = !solution.CheckPowersOfThree(21) ? "pass" : "fail";
            Console.WriteLine($"Case 3: {result}");
        }
    }
}

public class Program
{
    private static void Main()
    {
        Console.WriteLine("1780. Check if Number is a Sum of Powers of Three");
        
        Solution.Solution solution = new ();
        
        Solution.TestCases.Test1(solution);
        Solution.TestCases.Test2(solution);
        Solution.TestCases.Test3(solution);
    }
}