public class Solution
{
    public bool CanPartitionGrid(int[][] grid)
    {
        int rows = grid.Length;
        int cols = grid[0].Length;

        long total = 0;
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                total += grid[i][j];
            }
        }

        long currentSum = 0;
        long hTotal = total;
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                currentSum += grid[i][j];
                hTotal -= grid[i][j];
            }

            if (currentSum == hTotal)
            {
                return true;
            }
        }

        currentSum = 0;
        long vTotal = total;
        for(int j = 0; j < cols; j++)
        {
            for(int i = 0; i < rows; i++)
            {
                currentSum += grid[i][j];
                vTotal -= grid[i][j];
            }
            
            if (currentSum == vTotal)
            {
                return true;
            }
        }

        return false;
    }
}