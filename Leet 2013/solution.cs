public class DetectSquares
{
    struct Point
    {
        public int X { get; set; }
        public int Y { get; set; }
    }

    private readonly Dictionary<Point, int> _points = [];

    public DetectSquares()
    {

    }

    public void Add(int[] point)
    {
        var pt = new Point
        {
            X = point[0],
            Y = point[1]
        };

        _points[pt] = GetValueFromPoints(pt) + 1;
    }

    public int Count(int[] point)
    {
        var pt = new Point
        {
            X = point[0],
            Y = point[1]
        };

        int result = 0;
        foreach (var (key, _) in _points)
        {
            // Skip points that are on the same row or column as the given point
            if (pt.X == key.X || pt.Y == key.Y)
            {
                continue;
            }

            // Check if the distance between the given point and the current point is equal in both x and y directions
            int dx = Math.Abs(key.X - pt.X);
            int dy = Math.Abs(key.Y - pt.Y);
            if (dx != dy)
            {
                continue;
            }

            // Calculate the number of squares that can be formed with the given point and the current point
            var a = GetValueFromPoints(new Point { X = key.X, Y = pt.Y });
            var b = GetValueFromPoints(new Point { X = pt.X, Y = key.Y });
            var c = GetValueFromPoints(key);
            result += a * b * c;
        }

        return result;
    }

    // Helper method to get the value from the dictionary for a given point or return 0 if the point does not exist in the dictionary
    private int GetValueFromPoints(Point key)
    {
        if (_points.TryGetValue(key, out int value))
        {
            return value;
        }

        return 0;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("2013. Detect Squares");

        DetectSquares detectSquares = new();

        detectSquares.Add([3, 10]);
        detectSquares.Add([11, 2]);
        detectSquares.Add([3, 2]);
        Console.WriteLine($"Count squares with [11, 10]: {detectSquares.Count([11, 10])}");
        Console.WriteLine($"Count squares with [14, 8]: {detectSquares.Count([14, 8])}");
        detectSquares.Add([11, 2]);
        Console.WriteLine($"Count squares with [11, 10]: {detectSquares.Count([11, 10])}");
    }
}