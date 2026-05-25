public class Solution {
    private static int IntLength(int number) {
        if(number == 0)
        {
            return 1;
        }
        
        var abs = Math.Abs(number);
        var log = Math.Log10(abs);
        var floor = Math.Floor(log);
        return (int)floor + 1;
    }

    public int LongestCommonPrefix(int[] arr1, int[] arr2) {
        HashSet<int> seen = [];

        foreach(int number in arr1)
        {
            int current = number;
            while(current != 0 && !seen.Contains(current))
            {
                seen.Add(current);
                current /= 10;
            }
        }

        int result = 0;
        foreach(int number in arr2)
        {
            int current = number;
            while (current != 0 && !seen.Contains(current))
            {
                current /= 10;
            }

            if (current != 0)
            {
                result = Math.Max(result, IntLength(current));
            }
        }

        return result;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3043. Find the Length of the Longest Common Prefix");

        int[] arr1 = [1,10,100];
        int[] arr2 = [1000];

        Solution solution = new();
        int result = solution.LongestCommonPrefix(arr1, arr2);
        Console.WriteLine($"Longest common prefix between [1 10 100] and [1000] is {result}");
    }
}