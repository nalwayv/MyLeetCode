class Solution
{
    public bool SumGame(string num)
    {
        int left = 0;
        int right = 0;
        int sumLeft = 0;
        int sumRight = 0;

        for(int i = 0; i < num.Length / 2; i++)
        {
            // Left half of num
            if(num[i] == '?')
            {
                left++;
            }
            else
            {
                sumLeft += num[i] - '0';
            }

            // Right half of num
            if (num[num.Length - i - 1] == '?')
            {
                right++;
            }
            else
            {
                sumRight += num[num.Length - i - 1] - '0';
            }
        }

        var winCase1 = (left + right) % 2 == 1;
        var winCase2 = sumLeft - sumRight != (right - left) * 9 / 2;

        return winCase1 || winCase2;
    }
}

class Program
{
    private static void Main()
    {
        Solution solution = new();
        Console.WriteLine(!solution.SumGame("5023") ? "Pass" : "Fail");
        Console.WriteLine(solution.SumGame("23??") ? "Pass" : "Fail");
        Console.WriteLine(!solution.SumGame("?3295???") ? "Pass" : "Fail");
    }
}