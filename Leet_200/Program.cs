internal class Program
{
    private static bool Explore(int i, int j, int row, int col, char[][] grid, bool[,] vis)
    {
        if (i >= 0 && i < row && j >= 0 && j < col)
        {
            if (grid[i][j] == '1' && vis[i, j] != true)
            {
                vis[i, j] = true;

                Explore(i, j + 1, row, col, grid, vis);
                Explore(i, j - 1, row, col, grid, vis);
                Explore(i + 1, j, row, col, grid, vis);
                Explore(i - 1, j, row, col, grid, vis);
                return true;
            }
        }

        return false;
    }

    /// <summary>
    /// Count number of islands on grid
    /// </summary>
    /// <param name="grid">char[][]</param>
    /// <returns>number of islands found</returns>
    public static int NumberOfIslands(char[][] grid)
    {
        int row = grid.Length;
        int col = grid[0].Length;
        int count = 0;

        bool[,] vis = new bool[row, col];

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (Explore(i, j, row, col, grid, vis))
                {
                    count += 1;
                }
            }
        }

        return count;
    }

    private static void Main()
    {
        char[][] grid = [
            ['0', '0', '1'],
            ['1', '0', '1'],
            ['1', '0', '0'],
        ];
        int result = NumberOfIslands(grid);
        Console.WriteLine(result);
    }
}