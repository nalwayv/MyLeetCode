namespace Leet_594;

internal class Program
{
    public static int FindLHS(int[] nums) 
    {
        Dictionary<int, int> frequency = [];
        
        foreach (int num in nums) 
        {
            frequency[num] = frequency.TryGetValue(num, out int value) ? value + 1 : 1;
        }

        int result = 0;
        
        foreach (int key in frequency.Keys)
        {
            if (frequency.ContainsKey(key + 1))
            {
                result = int.Max(result, frequency[key] + frequency[key + 1]);
            }
        }

        return result;
    }
    
    static void Main()
    {
        Console.WriteLine("594. Longest Harmonious Subsequence");
        int result = FindLHS(new int[] { 1, 3, 2, 2, 5, 2, 3, 7 });
        Console.WriteLine(result);
    }
}