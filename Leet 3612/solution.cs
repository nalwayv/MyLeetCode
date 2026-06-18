using System.Text;

public class Solution 
{
    public string ProcessStr(string s) 
    {
        // '*' removes the last character from result, if it exists.
        // '#' duplicates the current result and appends it to itself.
        // '%' reverses the current result.

        StringBuilder sb = new();

        foreach(char ch in s)
        {
            if (ch >= 'a' && ch <= 'z')
            {
                sb.Append(ch);
            }

            if (ch == '*')
            {
                if(sb.Length > 0)
                {
                    sb = sb.Remove(sb.Length - 1, 1);
                }
            }
            
            if (ch == '#')
            {
                int len = sb.Length;
                for (int i = 0; i < len; i++)
                {
                    sb.Append(sb[i]);
                }
            }

            if (ch == '%')
            {
                var p1 = 0;
                var p2 = sb.Length - 1;
                while (p1 < p2)
                {
                    (sb[p2], sb[p1]) = (sb[p1], sb[p2]);
                    p1++;
                    p2--;
                }
            }
        } 

        return sb.ToString();
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3612. Process String with Special Operations I");

        Solution solution = new();
        
        Console.WriteLine($"Result: {solution.ProcessStr("ztv#*l")}");
        Console.WriteLine($"Result: {solution.ProcessStr("a#b%*")}");
    }
}