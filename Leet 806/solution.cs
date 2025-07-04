namespace Leet806;

class Program
{
    /// <summary>
    /// Calculates the number of lines required and the width of the last line
    /// when given character widths and a string.
    /// </summary>
    private static int[] NumberOfLines(int[] widths, string s)
    {
        if (widths.Length != 26)
        {
            return [0, 0];
        }

        const int maxWidth = 100;
        int lines = 1;
        int width = 0;

        foreach (char c in s)
        {
            int charWidth = widths[c - 'a'];
            if (width + charWidth > maxWidth)
            {
                lines++;
                width = charWidth;
            }
            else
            {
                width += charWidth;
            }
        }

        return [lines, width];
    }

    private static void Case1()
    {
        int[] width = { 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 };
        string s = "abcdefghijklmnopqrstuvwxyz";
        int[] result = NumberOfLines(width, s);
        Console.Write("[");
        foreach (int i in result)
        {
            Console.Write($" {i} ");
        }
        Console.WriteLine("]");
    }

    private static void Case2()
    {
        int[] width = { 4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 };
        string s = "bbbcccdddaaa";
        int[] result = NumberOfLines(width, s);
        Console.Write("[");
        foreach (int i in result)
        {
            Console.Write($" {i} ");
        }
        Console.WriteLine("]");
    }


    static void Main()
    {
        Console.WriteLine("806. Number of Lines To Write String");
        Case1();
        Case2();
    }
}