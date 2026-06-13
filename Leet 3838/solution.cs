using System.Text;

public class Solution
{
    public string MapWordWeights(string[] words, int[] weights)
    {
        StringBuilder sb = new();
        foreach (string word in words)
        {
            int sum = 0;
            foreach (char c in word)
            {
                // get ascii lowercase number between 0 and 25
                sum += weights[c - 'a'];
            }

            sum %= 26;

		    // results are mapped to a reversed alphabet where z = 0 and a = 25
		    // so we get the reversed index and convert it to a lowercase character
            int at = 26 - sum - 1;
            sb.Append((char)(at + 'a'));
        }

        return sb.ToString();
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3838. Weighted Word Mapping");

        Solution solution = new();

        string[] words = ["abcd", "def", "xyz"];
        int[] weights = [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2];
        string result = solution.MapWordWeights(words, weights);

        Console.WriteLine($"Result: {result}");
    }
}