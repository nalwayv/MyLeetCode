public class Solution
{
    public int MaxIncreaseKeepingSkyline(int[][] grid)
    {
        // store max value on each row and column
        var maxRows = new Dictionary<int, int>();
        var maxCols = new Dictionary<int, int>();
        for (int i = 0; i < grid.Length; i++)
        {
            for (int j = 0; j < grid[i].Length; j++)
            {
                maxRows[i] = maxRows.TryGetValue(i, out int maxRow) ? Math.Max(maxRow, grid[i][j]) : grid[i][j];
                maxCols[j] = maxCols.TryGetValue(j, out int maxCol) ? Math.Max(maxCol, grid[i][j]) : grid[i][j];
            }
        }

        int result = 0;
        for (int i = 0; i < grid.Length; i++)
        {
            for (int j = 0; j < grid[i].Length; j++)
            {
                result += Math.Abs(grid[i][j] - Math.Min(maxRows[i], maxCols[j]));
            }
        }

        return result;
    }
}