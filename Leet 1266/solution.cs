namespace Leet
{
    class Solution
    {
        public int MinTimeToVisitAllPoints(int[][] points)
        {
            int result = 0;
            for(int i = 0; i < points.Length - 1; i++)
            {
                int dx = int.Abs(points[i][0] - points[i+1][0]);
                int dy = int.Abs(points[i][1] - points[i+1][1]);

                int lo = int.Min(dx, dy);
                int hi = int.Max(dx, dy);

                result += lo + (hi - lo);
            }

            return result;
        }
    }
}


class Program
{
    private static void Main()
    {
        Console.WriteLine("1266. Minimum Time Visiting All Points");

        Leet.Solution solution = new();
        
        int[][] points = [[1,1],[3,4],[-1,0]];
        int case1 = solution.MinTimeToVisitAllPoints(points);
        string case1Result = case1 == 7 ? "pass":"fail";
        
        Console.WriteLine($"case1 should equal 7? {case1Result}");
    }
}