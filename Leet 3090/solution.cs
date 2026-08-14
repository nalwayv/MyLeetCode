class Solution
{
    public static int MaximumLengthSubstring(string s)
    {
        var frequency = new Dictionary<char, int>();
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.Length; right++)
        {
            if (!frequency.TryGetValue(s[right], out int value))
            {
                frequency[s[right]] = 0;
            } 
        
            frequency[s[right]] = value + 1;
            
            while (frequency[s[right]] > 2)
            {
                frequency[s[left]]--;
                left++;
            }

            maxLength = Math.Max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}

class Program
{
    private static void TestCase(string s, int expected)
    {
        string result = Solution.MaximumLengthSubstring(s) == expected ? "Pass" : "Fail";
        Console.WriteLine($"Test case should equal {expected} ? {result}");
    }

    private static void Main()
    {
        Console.WriteLine("3090. Maximum Length Substring With Two Occurrences");

        TestCase("bcbbbcba", 4);
        TestCase("aaaa", 2);
    }
}