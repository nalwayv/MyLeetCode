namespace LeetProblem
{
    public class Solution 
    {
        private static int ReversedInt(int n)
        {
            char[] chars = n.ToString().ToCharArray();
            Array.Reverse(chars);

            if (int.TryParse(new string(chars), out int result))
                return result;
            return 0;
        }

        public int MirrorDistance(int n) 
        {
            return int.Abs(n - ReversedInt(n));
        }
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3783. Mirror Distance of an Integer");
        
        LeetProblem.Solution solution = new();

        var testCase1 = solution.MirrorDistance(25);
        Console.WriteLine($"Result: {testCase1}");

        var testCase2 = solution.MirrorDistance(10);
        Console.WriteLine($"Result: {testCase2}");

        var testCase3 = solution.MirrorDistance(7);
        Console.WriteLine($"Result: {testCase3}");
    }
}