public class Solution
{
    public string KthDistinct(string[] arr, int k)
    {
        Dictionary<string, int> map = [];
        foreach (string s in arr)
        {
            if (map.ContainsKey(s))
            {
                map[s]++;
            }
            else
            {
                map[s] = 1;
            }
        }

        int i = 0;
        string[] tmp = new string[arr.Length];
        foreach (var item in map)
        {
            if (item.Value == 1)
            {
                tmp[i++] = item.Key;
            }
        }

        return (i < k) ? "" : tmp[k - 1];
    }
}

internal class Program
{

    private static void Example1(Solution sol)
    {
        string[] arr = ["d", "b", "c", "b", "c", "a"];
        int k = 2;

        string result = sol.KthDistinct(arr, k);
        Console.WriteLine($"Result: {result} == a");
    }

    private static void Example2(Solution sol)
    {
        string[] arr = ["aaa", "aa", "a"];
        int k = 1;

        string result = sol.KthDistinct(arr, k);
        Console.WriteLine($"Result: {result} == aaa");
    }

    private static void Example3(Solution sol)
    {
        string[] arr = ["a", "b", "a"];
        int k = 3;

        string result = sol.KthDistinct(arr, k);
        Console.WriteLine($"Result: {result} == ");
    }

    private static void Main(string[] args)
    {
        Console.WriteLine("2053. Kth Distinct String in an Array");
        Solution solution = new();

        Example1(solution);
        Example2(solution);
        Example3(solution);
    }
}