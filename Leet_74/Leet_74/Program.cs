namespace Leet_74;

internal abstract class Program
{
    private static void Case1(Solution solution)
    {
        int[][] matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]];
        bool result = solution.SearchMatrix(matrix, 20);
        Console.WriteLine($"Result: {result}");
    }

    private static void Main()
    {
        Console.WriteLine("74. Search a 2D Matrix");

        var solution = new Solution();
        Case1(solution);
    }
}