public class Solution 
{
    private static bool IsLowerChar(char ch) => 
        ch - 'a' >= 0 && ch - 'a' < 26;

    private static bool IsUpperChar(char ch) => 
        ch - 'A' >= 0 && ch - 'A' < 26;

    public int NumberOfSpecialChars(string word) 
    {
        Dictionary<char, int> table = [];
        for(int i = 0; i < word.Length; i++)
        {
            char ch = word[i];

            if (IsLowerChar(ch))
            {
                if(!table.ContainsKey(ch))
                    table[ch] = int.MinValue;

                table[ch] = int.Max(table[ch], i);
            }

            if (IsUpperChar(ch))
            {
                if(!table.ContainsKey(ch))
                    table[ch] = int.MaxValue;

                table[ch] = int.Min(table[ch], i);
            }
        }

        string lower = "abcdefghijklmnopqrstuvwxyz";
        string upper = lower.ToUpper();
        int count = 0;
        for(int i = 0; i < lower.Length; i++)
        {
            char low = lower[i];
            char upp = upper[i];

            if(table.ContainsKey(low) && table.ContainsKey(upp))
            {
                if (table[low] < table[upp])
                {
                    count++;
                }
            }
        }

        return count;
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("3121. Count the Number of Special Characters II");

        Solution solution = new();
        
        int count = solution.NumberOfSpecialChars("aabcdefghijklmnopqrstuvwxyzZYXWVUTSRQPONMLKJIHGFEDCBA");
        Console.WriteLine(count);
    }
}