namespace Leet841;
using System.Collections;

public class Solution
{
    public bool CanVisitAllRooms(IList<IList<int>> rooms)
    {
        Stack<int> keys = [];
        // int[] visited = new int[rooms.Count];

        BitArray b = new(rooms.Count);

        // setup
        for (int i = 0; i < rooms[0].Count; i++)
        {
            keys.Push(rooms[0][i]);
        }

        b.Set(0, true);
        // visited[0] = 1;

        while (keys.Count > 0)
        {
            int key = keys.Pop();

            // if (visited[key] == 1)
            if(b.Get(key))
            {
                continue;
            }
            b.Set(key, true);

            // visited[key] = 1;

            // collect keys for current room
            foreach (int newkey in rooms[key])
            {
                keys.Push(newkey);
            }
        }

        // if visited all rooms sum should be same as rooms count
        // return visited.Sum() == rooms.Count;

        return b.HasAllSet();
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("Leet 841 Rooms and Keys");
        Solution solution = new();

        IList<IList<int>> rooms1 = [[1], [2], [3], []];
        bool resultRooms1 = solution.CanVisitAllRooms(rooms1);
        Console.WriteLine($"Rooms 1: [[1],[2],[3],[]], Expect: true, Output: {resultRooms1}");

        IList<IList<int>> rooms2 = [[1, 3], [3, 0, 1], [2], [0]];
        bool resultRooms2 = solution.CanVisitAllRooms(rooms2);
        Console.WriteLine($"Rooms 2: [[1,3],[3,0,1],[2],[0]], Expect: true, Output: {resultRooms2}");

    }
}