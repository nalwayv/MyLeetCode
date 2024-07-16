// Leet 733 flood fill
public class Solution
{
    private struct Point
    {
        public int X;
        public int Y;
    }

    public int[][] FloodFill(int[][] image, int sr, int sc, int color)
    {
        int n = image.Length;
        int m = image[0].Length;
        
        int prev = image[sr][sc];
        if (prev != color) {
            Queue<Point> que = [];
            que.Enqueue(new Point { X = sr, Y = sc });

            while (que.Count > 0)
            {
                Point current = que.Dequeue();

                if (current.X < 0 || current.X >= n ||
                    current.Y < 0 || current.Y >= m ||
                    image[current.X][current.Y] != prev)
                {
                    continue;
                }

                image[current.X][current.Y] = color;
                que.Enqueue(new Point { X = current.X + 1, Y = current.Y });
                que.Enqueue(new Point { X = current.X - 1, Y = current.Y });
                que.Enqueue(new Point { X = current.X, Y = current.Y + 1 });
                que.Enqueue(new Point { X = current.X, Y = current.Y - 1 });
            }
        }

        return image;
    }
}

internal class Program
{
    private static void PrintImg(int[][] image)
    {
        for (int i = 0; i < image.Length; i++)
        {
            Console.Write("[");
            for (int j = 0; j < image[i].Length; j++)
            {
                Console.Write($" {image[i][j]} ");
            }
            Console.WriteLine("]");
        }
    }

    private static void Main()
    {
        Console.WriteLine("Leet 733!");

        Solution solution = new();

        Console.WriteLine("Image 1 ");
        int[][] img1 = [
            [1,1,1],
            [1,1,0],
            [1,0,1]
        ];
        /*
            [2,2,2],
            [2,2,0],
            [2,0,1],
        */
        int[][] result1 = solution.FloodFill(img1, 1, 1, 2);
        PrintImg(result1);

        Console.WriteLine("Image 2 ");
        int[][] img2 = [
            [0,0,0],
            [0,0,0],
        ];
        /*
            [0,0,0],
            [0,0,0],
        */
        int[][] result2 = solution.FloodFill(img2, 0, 0, 0);
        PrintImg(result2);

        Console.WriteLine("Image 3 ");
        int[][] img3 = [
            [0,0,0],
            [0,0,0],
        ];
        /*
            [2,2,2],
            [2,2,2],
        */
        int[][] result3 = solution.FloodFill(img3, 1, 0, 2);
        PrintImg(result3);

    }
}