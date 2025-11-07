class Leet2257
{
    public int CountUnguarded(int m, int n, int[][] guards, int[][] walls)
    {
        var blocked = new int[m, n];
        var guarded = new int[m, n];
        var directions = new (int dx, int dy)[] { (0, 1), (0, -1), (1, 0), (-1, 0) };

        foreach (var wall in walls)
        {
            blocked[wall[0], wall[1]] = 1;
        }

        foreach (var guard in guards)
        {
            blocked[guard[0], guard[1]] = 1;
        }

        foreach (var guard in guards)
        {
            foreach (var (dx, dy) in directions)
            {
                var x = guard[0] + dx;
                var y = guard[1] + dy;
                while (x >= 0 && x < m && y >= 0 && y < n && blocked[x, y] == 0)
                {
                    guarded[x, y] = 1;
                    x += dx;
                    y += dy;
                }
            }
        }

        int count = 0;
        for (int r = 0; r < m; r++)
        {
            for (int c = 0; c < n; c++)
            {
                if (guarded[r, c] == 0 && blocked[r, c] == 0)
                {
                    count++;
                }
            }
        }

        return count;
    }
}


class Program
{
    static void Main()
    {
        Console.WriteLine("2257. Count Unguarded Cells in the Grid");

        var leet2257 = new Leet2257();
        var guards = new int[][] { [0, 0], [1, 1], [2, 3] };
        var walls = new int[][] { [0, 1], [2, 2], [1, 4] };

        var case1 = leet2257.CountUnguarded(4, 6, guards, walls);
        Console.WriteLine(case1);
    }
}