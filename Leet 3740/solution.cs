public class Solution 
{
    public int MinimumDistance(int[] nums) 
    {
        Dictionary<int, List<int>> table = [];
        for(int i = 0; i < nums.Length; i++)
        {
            if(!table.ContainsKey(nums[i]))
            {
                table[nums[i]] = [];
            }
            table[nums[i]].Add(i);
        }

        int minDist = int.MaxValue;
        foreach(var values in table)
        {
            if(values.Value.Count < 3)
            {
                continue;
            }

            for(int i = 0; i < values.Value.Count - 2; i++)
            {
                var ij = int.Abs(values.Value[i] - values.Value[i + 1]);
                var jk = int.Abs(values.Value[i + 1] - values.Value[i + 2]);
                var ki = int.Abs(values.Value[i + 2] - values.Value[i]);
                minDist = Math.Min(minDist, ij + jk + ki);
            }
        }

        return minDist == int.MaxValue ? -1 : minDist;
    }
}


class Program
{
    private static void Main()
    {
        Console.WriteLine("3740. Minimum Distance Between Three Equal Elements I");

        Solution solution = new();
        Console.WriteLine(solution.MinimumDistance([1,2,1,1,3]));
        Console.WriteLine(solution.MinimumDistance([1,1,2,3,2,1,2]));
        Console.WriteLine(solution.MinimumDistance([1]));
    }
}