public class Solution 
{
    public int NumOfStrings(string[] patterns, string word) 
    {
        int count = 0;

        foreach(var pattern in patterns)
        {
            if (word.Contains(pattern))
            {
                count++;
            }
        }

        return count;
    }
}



class Program
{
    private static void Main()
    {
        Console.WriteLine("1967. Number of Strings That Appear as Substrings in Word");

        Solution solution = new();
        var count = solution.NumOfStrings(["a","abc","bc","d"], "abc");
        Console.WriteLine(count);
    }
}