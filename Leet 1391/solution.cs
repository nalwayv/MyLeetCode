public class Solution
{
    // NOTES:
    // 1. DFS
    // 2. Path starts at (0, 0)
    // 3. Path ends at (n - 1, m - 1)
    //
    // Grid Rules:
    // each tile is represented by a number 1-6 
    // each tile has multiple exit points up | down | left | right
    //
    //  +--u--+     +--u--+
    //  |     |     |     |
    //  l     r <-> l     r
    //  |     |     |     |
    //  +--d--+     +--d--+
    //

    private readonly Dictionary<int, List<(int x, int y)>> _directions = new() {
        {1, [(0, -1), (0, 1)]},
        {2, [(-1, 0), (1, 0)]},
        {3, [(0, -1), (1, 0)]},
        {4, [(0, 1), (1, 0)]},
        {5, [(0, -1), (-1, 0)]},
        {6, [(0, 1), (-1, 0)]}
    };

    public bool HasValidPath(int[][] grid)
    {
        var rows = grid.Length;
        var cols = grid[0].Length;

        Stack<(int, int)> stack = [];
        // Tracks the cells that have already been visited to avoid cycles.
        HashSet<(int, int)> visited = [];

        stack.Push((0, 0));
        while (stack.Count > 0)
        {
            (int cx, int cy) = stack.Pop();

            if (cx == rows - 1 && cy == cols - 1)
            {
                return true;
            }

            visited.Add((cx, cy));
            var currentTileType = grid[cx][cy];

            foreach (var (dx, dy) in _directions[currentTileType])
            {
                int nx = cx + dx;
                int ny = cy + dy;

                if (0 <= nx && nx < rows && 0 <= ny && ny < cols)
                {
                    var nextTileType = grid[nx][ny];
                    var oppositeDirection = (-dx, -dy);

                    // Check next has not been visited yet and
                    // that the next tile contains the opposite direction to the current direction
                    // so that they can link together.
                    var isUnvisited = !visited.Contains((nx, ny));
                    var hasOppositeDirection = _directions[nextTileType].Contains(oppositeDirection);

                    if (isUnvisited && hasOppositeDirection)
                    {
                        stack.Push((nx, ny));
                    }
                }
            }
        }

        return false;
    }
}


class Program
{
    private static void Main()
    {

        Console.WriteLine("1391. Check if There is a Valid Path in a Grid");

        // int[][] grid = [[2,4,3],[6,5,2]]; // true
        // int[][] grid = [[3, 4, 3, 4], [2, 2, 2, 2], [6, 5, 6, 5]]; // true
        // int[][] grid = [[1,2,1],[1,2,1]]; // false
        int[][] grid = [[2, 6, 3], [6, 5, 2]]; // false

        var solution = new Solution();

        var result = solution.HasValidPath(grid);
        string resultStr = result ? "true" : "false";
        Console.WriteLine($"Output: {resultStr}");
    }
}