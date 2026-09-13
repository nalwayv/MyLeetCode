Console.WriteLine("835. Image Overlap");

var solution = new Solution();

int[][] matrix1 = [[1,1,0],[0,1,0],[0,1,0]];
int[][] matrix2 = [[0,0,0],[0,1,1],[0,0,1]];
Console.WriteLine($"Result: {solution.LargestOverlap(matrix1, matrix2)}");

public class Solution
{
    public int LargestOverlap(int[][] img1, int[][] img2)
    {
        int rows = img1.Length;
        int cols = img1[0].Length;

        var coords1 = new List<(int, int)>();
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (img1[r][c] != 1)
                {
                    continue;
                }

                coords1.Add((r, c));
            }
        }

        var coords2 = new List<(int, int)>();
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (img2[r][c] != 1)
                {
                    continue;
                }
                coords2.Add((r, c));
            }
        }

        var frequency = new Dictionary<(int, int), int>();
        int maxV = 0;

        foreach (var (ax, ay) in coords1)
        {
            foreach (var (bx, by) in coords2)
            {
                var dist = (ax - bx, ay - by);

                if (!frequency.ContainsKey(dist))
                {
                    frequency[dist] = 0;
                }

                frequency[dist]++;
                maxV = Math.Max(frequency[dist], maxV);
            }
        }

        return maxV;
    }
}