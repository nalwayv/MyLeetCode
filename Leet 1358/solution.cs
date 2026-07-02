class Solution
{
    public static int NumberOfSubstrings(string str)
    {
        Dictionary<char, int> frequency = new(){
            {'a', 0},
            {'b', 0},
            {'c', 0}
        };

        int count = 0;
        int p1 = 0;
        for(int p2 = 0; p2 < str.Length; p2++)
        {
            if(!"abc".Contains(str[p2]))
                continue;

            frequency[str[p2]]++;

            while (frequency['a'] > 0 && frequency['b'] > 0 && frequency['c'] > 0)
            {
                count += str.Length - p2;

                frequency[str[p1]]--;
                p1++;
            }
        }

        return count;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("1358. Number of Substrings Containing All Three Characters");

        int count = Solution.NumberOfSubstrings("abcabc");
        Console.WriteLine($"Result `abcabc`: {count}");
    }
}