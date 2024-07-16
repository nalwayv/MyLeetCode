public class Solution
{
    public double MyPow(double x, int n)
    {
        if (n == 0)
        {
            return 1;
        }

        double pow = MyPow(x, n / 2);
        double squ = pow * pow;

        double result;
        if (n % 2 == 0)
        {
            result = squ;
        }
        else if (n > 0)
        {
            result = squ * x;
        }
        else
        {
            result = squ / x;
        }
        return result;
    }
}

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 50 Pow");

        Solution solution = new();

        Console.WriteLine($"{solution.MyPow(0.00001, 2147483647)} {Math.Pow(0.00001, 2147483647)}");
        Console.WriteLine($"{solution.MyPow(10.0, 2)} == {Math.Pow(10.0, 2)}");
        Console.WriteLine($"{solution.MyPow(11.00000, 2147483647)} {Math.Pow(11.00000, 2147483647)}");
    }
}