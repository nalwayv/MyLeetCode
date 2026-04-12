public class Solution
{
    public int MinimumDistance(int[] nums)
    {
        Dictionary<int, List<int>> table = [];
        for (int i = 0; i < nums.Length; i++)
        {
            if (!table.ContainsKey(nums[i]))
            {
                table[nums[i]] = [];
            }
            table[nums[i]].Add(i);
        }

        int result = int.MaxValue;
        foreach (var kvp in table)
        {
            if (kvp.Value.Count < 3)
            {
                continue;
            }

            for (int i = 0; i < kvp.Value.Count - 2; i++)
            {
                var ij = int.Abs(kvp.Value[i] - kvp.Value[i + 1]);
                var jk = int.Abs(kvp.Value[i + 1] - kvp.Value[i + 2]);
                var ki = int.Abs(kvp.Value[i + 2] - kvp.Value[i]);
                result = int.Min(result, ij + jk + ki);
            }
        }

        return result == int.MaxValue ? -1 : result;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3741. Minimum Distance Between Three Equal Elements II");
        Solution solution = new();
        int result = solution.MinimumDistance([1, 2, 1, 1, 3]);
        string passResult = result == 6 ? "pass" : "fail";
        Console.WriteLine($"[1,2,1,1,3] should equal 6? {passResult}");

    }
}