public class Solution 
{
    private readonly int _maxValue = int.MaxValue - 1;

    public int Reverse(int x)
    {
        if(x >= _maxValue || x <= -_maxValue)
        {
            return 0;
        }

        bool isNegative = false;
        if (x < 0)
        {
            isNegative = true;
            x *= -1;
        }

        Queue<int> que = [];
        int base10 = 10;
        while (x != 0)
        {
            que.Enqueue(x % base10);
            x /= base10;
        }

        // use long to catch over 32bit ints
        // when converting
        long result = 0;
        while (que.Count > 0)
        {
            if (result * base10 >= _maxValue)
            {
                return 0;
            }
            
            result *= base10;
            result += que.Dequeue();
        }

        return isNegative ? -(int)result : (int)result;
    }
}

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("7. Reverse Integer");
        // -2147483646 <-> +2147483646
        Solution solution = new();
        
        // 1534236469
        Console.WriteLine(solution.Reverse(1534236469));
        Console.WriteLine(-2147483648 <= int.MaxValue - 1);

    }
}