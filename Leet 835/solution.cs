Console.WriteLine("835. Image Overlap");

int[,] matrix1 = new int[,] { { 1, 1, 0 }, { 0, 1, 0 }, { 0, 1, 0 } };
int[,] matrix2 = new int[,] { { 0, 0, 0 }, { 0, 1, 1 }, { 0, 0, 1 } };
Console.WriteLine($"Result: {Solution.LargestOverlap(matrix1, matrix2)}");


public class Solution
{
    public static int LargestOverlap(int[,] img1, int[,] img2)
    {
        int rows = img1.GetLength(0);
        int cols = img1.GetLength(1);

        var coordsImg1 = new List<(int, int)>();
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (img1[r, c] == 1)
                {
                    coordsImg1.Add((r, c));
                }
            }
        }

        var coordsImg2 = new List<(int, int)>();
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (img2[r, c] == 1)
                {
                    coordsImg2.Add((r, c));
                }
            }
        }

        var frequency = new Dictionary<(int, int), int>();
        int maxFrequency = 0;

        foreach (var (ax, ay) in coordsImg1)
        {
            foreach (var (bx, by) in coordsImg2)
            {
                var dist = (ax - bx, ay - by);

                if (!frequency.TryGetValue(dist, out int value))
                {
                    value = 0;
                    frequency[dist] = value;
                }

                frequency[dist] = ++value;
                maxFrequency = Math.Max(value, maxFrequency);
            }
        }

        return maxFrequency;
    }
}