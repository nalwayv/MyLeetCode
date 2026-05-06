using System.ComponentModel;
using System.IO.Pipelines;

public class Solution 
{
    public static void PrintGrid(char[][] grid)
    {
        foreach(var row in grid)
        {
            Console.Write("[");
            foreach(var val in row)
            {
                Console.Write($" {val} ");
            }
            Console.WriteLine("]");
        }
    }

    public char[][] RotateTheBox(char[][] boxGrid) 
    {
        int n = boxGrid.Length;
        int m = boxGrid[0].Length;

        char[][] result = new char[m][];

        // Rotate

        for(int col = 0; col < m; col++)
        {
            char[] chars = new char[n];

            for(int row = n - 1; row >= 0; row--)
            {
                chars[row] = boxGrid[n - row - 1][col];
            }

            result[col] = chars;
        }

        // Simulate

        for(int col = 0; col < n; col++)
        {
            int k = m - 1;
            for(int row = m - 1; row >= 0; row--)
            {
                if(result[row][col] == '*')
                {
                    // reset back
                    k = row - 1;
                }
                else if(result[row][col] == '#')
                {
                    // swap
                    // var tmp = result[row][col];
                    // result[row][col] = result[k][col];
                    // result[k][col] = tmp;
                    result[row][col] = '.';
                    result[k][col] = '#';
                    k--;
                }
            }
        }

        return result;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("1861. Rotating the Box");

        Solution solution = new();
        char[][] grid1 = [
            ['#', '.', '#']];

        char[][] grid2 =  [
            ['#','.','*','.'],
            ['#','#','*','.']];

        char[][] grid3 = [
            ['#','#','*','.','*','.'],
            ['#','#','#','*','.','.'],
            ['#','#','#','.','#','.']];
            
        char[][] result = solution.RotateTheBox(grid3);
        Solution.PrintGrid(result);
    }
}