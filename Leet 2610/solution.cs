public class Solution
{
    public IList<IList<int>> FindMatrix(int[] nums)
    {
        var table = new Dictionary<int, int>();
        var result = new List<IList<int>>();

        foreach (var num in nums)
        {
            table.TryAdd(num, 0);
            var freq = table[num];

            if (freq >= result.Count)
            {
                result.Add(new List<int>());
            }

            result[freq].Add(num);
            table[num]++;
        }

        return result;
    }
}