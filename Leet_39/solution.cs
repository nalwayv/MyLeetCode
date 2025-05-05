namespace Leet39;

public class Solution 
{
    private readonly IList<IList<int>> _result = [];
    private readonly List<int> _current = [];

    /// <summary>
    /// Recursively finds combinations of numbers that sum up to the target value.
    /// </summary>
    private void FindCombinations(int[] candidates, int target, int start)
    {
        if (target < 0)
        {
            return;
        }

        if (target == 0)
        {
            _result.Add(new List<int>(_current));
            return;
        }

        for (int i = start; i < candidates.Length; i++)
        {
            _current.Add(candidates[i]);
            FindCombinations(candidates, target - candidates[i], i);
            _current.RemoveAt(_current.Count - 1);
        }   
    }

    /// <summary>
    /// Finds all unique combinations of candidates where the chosen numbers sum to the target.
    /// Each number within candidates may be used an unlimited number of times.
    /// </summary>
    public IList<IList<int>> CombinationSum(int[] candidates, int target) 
    {
        _result.Clear();
        _current.Clear();
        
        FindCombinations(candidates, target, 0);
        
        return _result;
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("39. Combination Sum");

        Solution solution = new();
        IList<IList<int>> result = solution.CombinationSum([2, 3, 6, 7], 7);

        foreach (var item in result)
        {
            Console.Write("[");
            foreach (var item2 in item)
            {
                Console.Write($" {item2} ");
            }
            Console.WriteLine("]");
        }
    }
}