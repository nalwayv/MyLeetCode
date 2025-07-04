using System.Text;

public class Solution
{
    private struct RomanSymbol
    {
        public int Number;
        public string Symbol;
    }

    public string IntToRoman(int num)
    {
        RomanSymbol[] symbols = [
            new RomanSymbol {Number = 1000, Symbol = "M"},
            new RomanSymbol {Number = 900,  Symbol = "CM"},
            new RomanSymbol {Number = 500,  Symbol = "D"},
            new RomanSymbol {Number = 400,  Symbol = "CD"},
            new RomanSymbol {Number = 100,  Symbol = "C"},
            new RomanSymbol {Number = 90,   Symbol = "XC"},
            new RomanSymbol {Number = 50,   Symbol = "L"},
            new RomanSymbol {Number = 40,   Symbol = "XL"},
            new RomanSymbol {Number = 10,   Symbol = "X"},
            new RomanSymbol {Number = 9,    Symbol = "IX"},
            new RomanSymbol {Number = 5,    Symbol = "V"},
            new RomanSymbol {Number = 4,    Symbol = "IV"},
            new RomanSymbol {Number = 1,    Symbol = "I"},
        ];

        // Build string of roman symbols
        StringBuilder sb = new();
        foreach (RomanSymbol sym in symbols)
        {
            int count = num / sym.Number;
            if (count > 0)
            {
                num %= sym.Number;
                for (int i = 0; i < count; i++)
                {
                    sb.Append(sym.Symbol);
                }
            }
        }

        return sb.ToString();
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("Leet 12. Integer To Roman");
        Solution solution = new();

        Console.WriteLine(solution.IntToRoman(3749) == "MMMDCCXLIX");
        Console.WriteLine(solution.IntToRoman(1994) == "MCMXCIV");
        Console.WriteLine(solution.IntToRoman(4520) == "MMMMDXX");
        Console.WriteLine(solution.IntToRoman(4) == "IV");
        Console.WriteLine(solution.IntToRoman(5) == "V");
        Console.WriteLine(solution.IntToRoman(3) == "III");
    }
}