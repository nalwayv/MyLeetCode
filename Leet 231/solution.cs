namespace Leet231;

class Solution
{
    public bool IsPowerOfTwo(int n)
    {
        if (n == 0)
        {
            return false;
        }

        while (n % 2 == 0)
        {
            n /= 2;
        }

        return n == 1;
    }
}

internal class Program
{
    static void Main()
    {
        Console.WriteLine("231. Power of Two");

        Solution sol = new();

        Console.WriteLine($"1 should be a power of 2? {sol.IsPowerOfTwo(1)}");
        Console.WriteLine($"16 should be a power of 2? {sol.IsPowerOfTwo(16)}");
        Console.WriteLine($"13 should not be a power of 2? {!sol.IsPowerOfTwo(13)}");
    }
}