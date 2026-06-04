namespace Leet
{
    public class Solution
    {
        public static int TotalWaviness(int num1, int num2)
        {
            int result = 0;
            for (int i = num1; i <= num2; i++)
            {
                var num = Convert.ToString(i);
                if (num.Length < 3)
                    continue;

                int count = 0;
                for (int j = 0; j <= num.Length - 3; j++)
                {
                    ReadOnlySpan<char> current = num.AsSpan(j, 3);
                    bool peak = current[1] > current[0] && current[1] > current[2];
                    bool valley = current[1] < current[0] && current[1] < current[2];

                    if (peak || valley)
                        count++;

                }

                result += count;
            }
            return result;
        }
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("3751. Total Waviness of Numbers in Range I");

        int waviness = Leet.Solution.TotalWaviness(120, 130);
        Console.WriteLine($"Waviness between 120 and 130 is {waviness}");
    }
}