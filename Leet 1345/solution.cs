public class Solution
{
    public int MinJumps(int[] arr)
    {
        Dictionary<int, List<int>> graph = new();
        for (int i = 0; i < arr.Length; i++)
        {
            int value = arr[i];
            if (!graph.ContainsKey(value))
            {
                graph[value] = new();
            }
            graph[value].Add(i);
        }

        Queue<(int, int)> que = new();
        HashSet<int> seen = new();

        que.Enqueue((0, 0));

        while (que.Count > 0)
        {
            (int index, int distance) = que.Dequeue();

            if (seen.Contains(index))
            {
                continue;
            }

            seen.Add(index);

            if (index == arr.Length - 1)
            {
                return distance;
            }

            List<int> neighbours = graph[arr[index]];
            neighbours.Add(index + 1);
            neighbours.Add(index - 1);

            foreach (int neighbour in neighbours)
            {
                if (0 <= neighbour && neighbour < arr.Length)
                {
                    que.Enqueue((neighbour, distance + 1));
                }
            }

            neighbours.Clear();
        }

        return -1;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("345. Jump Game IV");
        Solution solution = new();

        int[] arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404];
        int minJumps = solution.MinJumps(arr);
        Console.WriteLine($"MinJumps: {minJumps}");
    }
}