public class Solution
{
    private readonly List<(int, int)> _directions = [(0, 1), (0, -1), (1, 0), (-1, 0)];
    private readonly HashSet<(int, int)> _visited = [];

    /// <summary>
    /// Helper function to check if there is a cycle starting from the given position (i, j) in the grid.
    /// </summary>
    /// <param name="i"></param>
    /// <param name="j"></param>
    /// <param name="grid"></param>
    /// <returns>boolean indicating if a cycle exists</returns>
    private bool HasCycle(int i, int j, char[][] grid)
    {
        Stack<(int, int, int, int)> stack = new Stack<(int, int, int, int)>();
        stack.Push((i, j, -1, -1));

        while (stack.Count > 0)
        {
            (int cx, int cy, int px, int py) = stack.Pop();
            _visited.Add((cx, cy));

            foreach ((int dx, int dy) in _directions)
            {
                int nx = cx + dx;
                int ny = cy + dy;

                // Check if the new position is within bounds
                if (!(0 <= nx && nx < grid.Length && 0 <= ny && ny < grid[0].Length))
                {
                    continue;
                }

                // Check if the character at the new position is the same as the current position
                if (grid[cx][cy] != grid[nx][ny])
                {
                    continue;
                }

                // Check if the new position has been visited and is not the parent of the current position
                if (_visited.Contains((nx, ny)) && !(nx == px && ny == py))
                {
                    return true;
                }

                // If the new position has not been visited, add it to the stack
                if (!_visited.Contains((nx, ny)))
                {
                    stack.Push((nx, ny, cx, cy));
                }
            }
        }

        return false;
    }

    /// <summary>
    /// Given a 2D grid of characters, return true if there is a cycle in the grid, or false otherwise.
    /// </summary>
    /// <param name="grid">2d array of characters</param>
    /// <returns>boolean indicating if a cycle exists</returns>
    public bool ContainsCycle(char[][] grid)
    {
        _visited.Clear();

        for (int i = 0; i < grid.Length; i++)
        {
            for (int j = 0; j < grid[0].Length; j++)
            {
                if (_visited.Contains((i, j)))
                {
                    continue;
                }

                if (HasCycle(i, j, grid))
                {
                    return true;
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
        Console.WriteLine("1559. Detect Cycles in 2D Grid");

        char[][] grid = [
            ['a', 'a', 'a', 'a', 'a'],
            ['a', 'b', 'b', 'b', 'a'],
            ['a', 'b', 'b', 'b', 'a'],
            ['a', 'a', 'a', 'a', 'a'],
        ];

        Solution solution = new();

        string case1Result = solution.ContainsCycle(grid) ? "Pass" : "Fail";
        Console.WriteLine($"Cycle detected? {case1Result}");
    }
}