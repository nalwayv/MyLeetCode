class Solution
{
    private static int MaxDepth(Dictionary<int, List<int>> tree, int root)
    {
        if (!tree.ContainsKey(root))
        {
            return 0;
        }

        int depth = 0;
        foreach (int child in tree[root])
        {
            depth = int.Max(depth, MaxDepth(tree, child) + 1);
        }

        return depth;
    }

    private static (Dictionary<int, List<int>> Tree, int Root) BuildTree(int[][] edges)
    {
        Dictionary<int, List<int>> tree = [];
        int root = 0;

        foreach (var edge in edges)
        {
            if (edge.Length != 2)
            {
                continue;
            }

            int parent = edge[0];
            int child = edge[1];

            if (!tree.ContainsKey(parent))
            {
                tree[parent] = [];
                root += parent;
            }

            if (!tree.ContainsKey(child))
            {
                tree[child] = [];
                root += child;
            }

            tree[parent].Add(child);
            root -= child;
        }

        return (tree, root);
    }

    public int AssignEdgeWeights(int[][] edges)
    {
        var (tree, root) = BuildTree(edges);
        // big int version of 2 ** depth -1 % 1000000007
        return (int)System.Numerics.BigInteger.ModPow(
            2,
            MaxDepth(tree, root) - 1,
            1000000007
        );
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3558. Number of Ways to Assign Edge Weights I");
        int[][] edges = [[1, 2], [1, 3], [3, 4], [3, 5]];

        Solution solution = new();
        int result = solution.AssignEdgeWeights(edges);
        
        Console.WriteLine($"Result: {result}");

    }
}