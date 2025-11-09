class Leet2169
{
    public int CountOperations(int num1, int num2)
    {
        if (num1 == 0 || num2 == 0)
        {
            return 0;
        }

        int count = 0;
        while (true)
        {
            if (num1 > num2)
            {
                num1 -= num2;
            }
            else
            {
                num2 -= num1;
            }

            count++;

            if (num1 <= 0 || num2 <= 0)
            {
                return count;
            }
        }
    }
}


class Program
{
    private static void Leet2169_Test()
    {
        Console.WriteLine("2169. Count Operations to Obtain Zero");

        var leet2169 = new Leet2169();

        Console.WriteLine($"{leet2169.CountOperations(2, 3)} == 3");
        Console.WriteLine($"{leet2169.CountOperations(10, 10)} == 1");
        Console.WriteLine($"{leet2169.CountOperations(11, 2)} == 7");
    }

    static void Main()
    {
        Leet2169_Test();
    }
}