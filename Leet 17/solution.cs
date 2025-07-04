using System.Text;

namespace Leet17;

public class Solution
{
    private readonly Dictionary<char, string> _table = new()
    {
        { '2', "abc" },
        { '3', "def" },
        { '4', "ghi" },
        { '5', "jkl" },
        { '6', "mno" },
        { '7', "pqrs" },
        { '8', "tuv" },
        { '9', "wxyz" }
    };

    private void Backtrack(IList<string> result, StringBuilder builder, string digits, int index)
    {
        if (index == digits.Length)
        {
            result.Add(builder.ToString());
            return;
        }

        foreach (var digit in _table[digits[index]])
        {
            builder.Append(digit);
            Backtrack(result, builder, digits, index + 1);
            builder.Length -= 1;
        }
    }

    public IList<string> LetterCombinations(string digits)
    {
        if (digits.Length == 0)
        {
            return [];
        }

        var result = new List<string>();
        var builder = new StringBuilder();
        Backtrack(result, builder, digits, 0);
        return result;
    }
}

static class Program
{
    private static void Main()
    {
        Console.WriteLine("17. Letter Combinations of a Phone Number");
        
        Solution solution = new();
        IList<string> result = solution.LetterCombinations("23");
        Console.WriteLine($"[{string.Join(", ", result)}]");
    }
}