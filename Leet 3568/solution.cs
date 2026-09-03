class Solution
{
    private static (int x, int y) FindStart(string[] classroom)
    {
        for(int i = 0; i < classroom.Length; i++)
        {
            var j = classroom[i].IndexOf('S');
            if (j != -1)
            {
                return (i, j);
            }
        }

        return (-1, -1);
    }

    public static int MinMoves(string[] classroom, int energy)
    {
        if (classroom.Length == 0 || classroom[0].Length == 0)
        {
            return -1;
        }

        var (x, y) = FindStart(classroom);
        if (x == -1 || y == -1)
        {
            return -1;
        }

        var rows = classroom.Length;
        var cols = classroom[0].Length;

        var litter = new Dictionary<int, int>();
        var id = 0;
        for (var r = 0; r < rows; r++)
        {
            for (var c = 0; c < cols; c++)
            {
                if (classroom[r][c] == 'L')
                {
                    litter.Add(r * cols + c, id++);
                }
            }
        }

        var target = (1 << litter.Count) - 1;

        var best = new int[target + 1, rows, cols];
        for (var i = 0; i < best.GetLength(0); i++)
        {
            for (var j = 0; j < best.GetLength(1); j++)
            {
                for (var k = 0; k < best.GetLength(2); k++)
                {
                    best[i, j, k] = -1;
                }
            }
        }

        var directions = new[] { (0, 1), (0, -1), (1, 0), (-1, 0) };

        var queue = new Queue<(int row, int col, int mask, int remainingEnergy, int steps)>();
        queue.Enqueue((x, y, 0, energy, 0));

        while (queue.Count > 0)
        {
            var (row, col, mask, remainingEnergy, steps) = queue.Dequeue();

            if (classroom[row][col] == 'R')
            {
                remainingEnergy = energy;
            }

            if (litter.TryGetValue(row * cols + col, out var litterId))
            {
                mask |= 1 << litterId;
            }

            if (mask == target)
            {
                return steps;
            }

            if (best[mask, row, col] >= remainingEnergy)
            {
                continue;
            }

            best[mask, row, col] = remainingEnergy;

            if (remainingEnergy == 0)
            {
                continue;
            }

            foreach (var (dx, dy) in directions)
            {
                var nextRow = row + dx;
                var nextCol = col + dy;

                if (nextRow < 0 || nextCol < 0 || nextRow >= rows || nextCol >= cols)
                {
                    continue;
                }

                if (classroom[nextRow][nextCol] == 'X')
                {
                    continue;
                }

                queue.Enqueue((nextRow, nextCol, mask, remainingEnergy - 1, steps + 1));
            }
        }

        return -1;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3568. Minimum Moves to Clean the Classroom");

        int result = Solution.MinMoves(["S.", "XL"], 2);
        Console.WriteLine($"Result: {result}");
    }
}