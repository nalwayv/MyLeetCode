public class Solution
{
    // Pattern
    // (n=3, k=2)
    //     1 2 3 4
    //   +--------
    // 1 | 0
    // 2 | 0 1
    // 3 | 0 1 1 0
    //       -

    private int SolveK(int num, int n, int k)
    {
        if (n == 1)
        {
            return num;
        }

        int l = 1 << (n - 1);

        int result;
        if (k <= l / 2)
        {
            result = SolveK(num, n - 1, k);
        }
        else
        {
            result = SolveK(1 - num, n - 1, k - l / 2);
        }
        return result;

    }

    public int KthGrammar(int n, int k)
    {
        return SolveK(0, n, k);
    }
}

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 779");

        Solution solution = new();
        Console.WriteLine($"Output {solution.KthGrammar(4, 1)}");
        Console.WriteLine($"Output {solution.KthGrammar(2, 2)}");
    }
}