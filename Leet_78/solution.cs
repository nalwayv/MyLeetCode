namespace Leet78;

public class Solution
{
    /// <summary>
    /// Generates all possible subsets in an array of integers.
    /// This method is a recursive helper function that explores all possibilities
    /// by including or excluding each element.
    /// </summary>
    private static void GenerateSubsets(IList<IList<int>> allSubsets, IList<int> currentSubset, int[] numbers, int currentPosition = 0)
    {
        if (currentPosition == numbers.Length)
        {
            allSubsets.Add(new List<int>(currentSubset));
            return;
        }

        // Exclude
        GenerateSubsets(allSubsets, currentSubset, numbers, currentPosition + 1);

        // Include
        currentSubset.Add(numbers[currentPosition]);
        GenerateSubsets(allSubsets, currentSubset, numbers, currentPosition + 1);
        currentSubset.RemoveAt(currentSubset.Count - 1);
    }
    
    public IList<IList<int>> Subsets(int[] nums)
    {
        IList<int> currentSubset = [];
        IList<IList<int>> allSubsets = [];
        GenerateSubsets(allSubsets, currentSubset, nums);
        return allSubsets;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("78. Subsets");
        Solution solution = new();
        
        IList<IList<int>> result = solution.Subsets([ 1, 2, 3 ]);
        foreach (var subset in result)
        {
            Console.WriteLine($"[{string.Join(", ", subset)}]");
        }

    }
}