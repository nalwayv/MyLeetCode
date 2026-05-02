using System.Text;

public class Solution
{
    public int RotatedDigits(int n)
    {
        Dictionary<char, char> flippedNumbers = new()
        {
            {'0', '0'},
            {'1', '1'},
            {'2', '5'},
            {'5', '2'},
            {'6', '9'},
            {'8', '8'},
            {'9', '6'},
        };

        int count = 0;
        for(int i = 1; i <= n; i++)
        {
            string strNum = i.ToString();
            string flippedNum = new string(strNum
                .Select(x => flippedNumbers.GetValueOrDefault(x, '_'))
                .ToArray());

            
            if(flippedNum.Contains('_'))
            {
                continue;
            }

            if(strNum == flippedNum)
            {
                continue;
            }
            
            count++;
        }

        return count;
    }
}
class Program
{
    private static void Main()
    {
        Console.WriteLine("788. Rotated Digits");
        Solution solution = new();
        int case1 = solution.RotatedDigits(10);
        string case1Result = case1 == 4 ? "Pass" : "Fail";
        Console.WriteLine($"Rotated Digits 10 should equal 4: {case1Result}");
    }
}