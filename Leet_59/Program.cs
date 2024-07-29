
public class SolutionException
    : Exception
{
    public SolutionException(string? message)
        : base(message)
    {
    }
}

public class Solution
{
    private enum Direction
    {
        LEFT, RIGHT, UP, DOWN
    }

    public void PrintMatrix(int[][] mat)
    {
        for (int i = 0; i < mat.Length; i++)
        {
            Console.Write("[");
            for (int j = 0; j < mat.Length; j++)
            {
                Console.Write(" {0:D2} ", mat[i][j]);
            }
            Console.WriteLine("]");
        }
    }

    private bool InRange(int x, int y, int n)
    {
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    private int[][] NewMatrix(int n)
    {
        int[][] matrix = new int[n][];
        for (int i = 0; i < n; i++)
        {
            matrix[i] = new int[n];
        }
        return matrix;
    }

    public int[][] GenerateMatrix(int n)
    {
        if (n < 1 || n > 20)
        {
            throw new SolutionException("n has to be between 1 and 20");
        }

        int[][] matrix = NewMatrix(n);
        bool[,] visited = new bool[n, n];

        matrix[0][0] = 1;
        visited[0, 0] = true;

        int i = 1;
        int end = n * n;
        int x = 0;
        int y = 0;
        Direction dir = Direction.LEFT;

        while (i < end)
        {
            switch (dir)
            {
                case Direction.LEFT:
                    if (InRange(x, y + 1, n) && !visited[x, y + 1])
                    {
                        y += 1;
                        i += 1;

                        matrix[x][y] = i;
                        visited[x, y] = true;
                    }
                    else
                    {
                        dir = Direction.DOWN;
                    }
                    break;

                case Direction.DOWN:
                    if (InRange(x + 1, y, n) && !visited[x + 1, y])
                    {
                        x += 1;
                        i += 1;

                        visited[x, y] = true;
                        matrix[x][y] = i;
                    }
                    else
                    {
                        dir = Direction.RIGHT;
                    }
                    break;

                case Direction.RIGHT:
                    if (InRange(x, y - 1, n) && !visited[x, y - 1])
                    {
                        y -= 1;
                        i += 1;

                        visited[x, y] = true;
                        matrix[x][y] = i;
                    }
                    else
                    {
                        dir = Direction.UP;
                    }
                    break;

                case Direction.UP:
                    if (InRange(x - 1, y, n) && !visited[x - 1, y])
                    {
                        x -= 1;
                        i += 1;

                        visited[x, y] = true;
                        matrix[x][y] = i;
                    }
                    else
                    {
                        dir = Direction.LEFT;
                    }
                    break;
            }
        }

        return matrix;
    }
}

internal class Program
{
    private static void Matrix3x3(Solution sol)
    {
        Console.WriteLine("Matrix  3x3");

        int[][] matrix = sol.GenerateMatrix(3);
        sol.PrintMatrix(matrix);
    }

    private static void Matrix1x1(Solution sol)
    {
        Console.WriteLine("Matrix  1x1");
        int[][] matrix = sol.GenerateMatrix(1);
        sol.PrintMatrix(matrix);
    }

    private static void Matrix5x5(Solution sol)
    {
        Console.WriteLine("Matrix  5x5");
        int[][] matrix = sol.GenerateMatrix(5);
        sol.PrintMatrix(matrix);
    }

    private static void Main()
    {
        Console.WriteLine("Leet 59. Spiral Matrix II");

        Solution solution = new();
        Matrix3x3(solution);
        Matrix1x1(solution);
        Matrix5x5(solution);
    }
}