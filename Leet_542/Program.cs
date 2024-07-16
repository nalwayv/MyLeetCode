using System.Xml;

namespace Leet542;

public class Solution
{
    private struct Point
    {
        public int X;
        public int Y;
    }

    public int[][] UpdateMatrix(int[][] mat)
    {
        int row = mat.Length;
        int col = mat[0].Length;

        Point[] directions = [
            new Point {X = 1, Y = 0},
            new Point {X = -1, Y = 0},
            new Point {X = 0, Y = 1},
            new Point {X = 0, Y = -1},
        ];

        Queue<Point> que = [];

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (mat[i][j] != 0)
                {
                    mat[i][j] = int.MaxValue;
                }
                else
                {
                    que.Enqueue(new Point { X = i, Y = j });
                }
            }
        }

        while (que.Count > 0)
        {
            Point curr = que.Dequeue();

            foreach (Point dir in directions)
            {
                int px = curr.X;
                int py = curr.Y;

                int dx = px + dir.X;
                int dy = py + dir.Y;

                if (dx >= 0 && dx < row && dy >= 0 && dy < col)
                {
                    if (mat[dx][dy] > mat[px][py] + 1)
                    {
                        mat[dx][dy] = mat[px][py] + 1;
                        que.Enqueue(new Point { X = dx, Y = dy });
                    }
                }
            }
        }

        return mat;
    }
}

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 542 01 Matrix");

        Solution solution = new();

        Console.WriteLine("Matrix 1");
        int[][] matrix1 = [
            [0,0,1],
            [0,1,1],
            [1,1,1],
        ];
        matrix1 = solution.UpdateMatrix(matrix1);
        for (int i = 0; i < 3; i++)
        {
            Console.Write("[");
            for (int j = 0; j < 3; j++)
            {
                Console.Write($" {matrix1[i][j]} ");
            }
            Console.WriteLine("]");
        }

    }
}