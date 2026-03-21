class Solutuion
{
    public int[][] ReverseSubmatrix(int[][] grid, int x, int y, int k)
    {
        int endRow = int.Min(x + k, grid.Length);
        int endCol = int.Min(y + k, grid[0].Length);
        List<Tuple<int, int, int>> values = [];
        
        int row = x;
        for(int r = endRow - 1; r >= x; r--)
        {
            for (int c = y; c < endCol; c++)
            {
                values.Add(Tuple.Create(row, c, grid[r][c]));
            }
            row++;
        }

        foreach (var (newX, newY, value) in values)
        {
            grid[newX][newY] = value;
        }
        
        return grid;
    }
}