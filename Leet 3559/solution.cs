public class Solution
{
    private static (Dictionary<int, List<int>> Tree, int root) BuildTree(int[][] edges)
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

    // private static void Dsf(Dictionary<int, int> depths, Dictionary<int, List<int>> tree, int root, int depth)
    // {
    //     if(!tree.ContainsKey(root))
    //     {
    //         return;
    //     }

    //     if (!depths.ContainsKey(root)) 
    //     {
    //         depths[root] = 0;
    //     }

    //     depths[root] = int.Max(depths[root], depth);

    //     foreach(var child in tree[root])
    //     {
    //         Dsf(depths, tree, child, depth + 1);
    //     }
    // }

    private static Dictionary<int, int> GetDepths(Dictionary<int, List<int>> tree, int root)
    {
        Dictionary<int, int> depths = [];
        // Dsf(depths, tree, root, 0);

        Stack<(int, int)> stk = [];
        stk.Push((root, 0));

        while (stk.Count > 0)
        {
            var (curr, depth) = stk.Pop();

            if (!depths.ContainsKey(curr))
            {
                depths[curr] = 0;
            }

            depths[curr] = int.Max(depths[curr], depth);

            foreach (var child in tree[curr])
            {
                stk.Push((child, depth + 1));
            }
        }

        return depths;
    }

    private static Dictionary<int, int> GetParents(int[][] edges)
    {
        Dictionary<int, int> parents = [];

        foreach (var edge in edges)
        {
            if (edge.Length != 2)
            {
                continue;
            }

            int parent = edge[0];
            int child = edge[1];

            parents[child] = parent;
        }

        return parents;
    }

    private static int GetLowestCommonAncestor(int node1, int node2, Dictionary<int, int> parents, Dictionary<int, int> depths)
    {
        while (depths[node1] > depths[node2])
        {
            node1 = parents[node1];
        }

        while (depths[node2] > depths[node1])
        {
            node2 = parents[node2];
        }

        while (node1 != node2)
        {
            node1 = parents[node1];
            node2 = parents[node2];
        }

        return node1;
    }

    private static int BigNumber(int exponent)
    {
        if (exponent < 0)
        {
            return 0;
        }

        return (int)System.Numerics.BigInteger.ModPow(
            2,
            exponent,
            1000000007
        );
    }

    public int[] AssignEdgeWeights(int[][] edges, int[][] queries)
    {
        var (tree, root) = BuildTree(edges);

        Dictionary<int, int> depths = GetDepths(tree, root);
        Dictionary<int, int> parents = GetParents(edges);

        int[] result = new int[queries.Length];
        
        int i = 0;
        foreach (var query in queries)
        {
            if (query.Length != 2)
            {
                continue;
            }

            int node1 = query[0];
            int node2 = query[1];
            var lcaNode = GetLowestCommonAncestor(node1, node2, parents, depths);

            var distanceNode1 = depths[node1] - depths[lcaNode];
            var distanceNode2 = depths[node2] - depths[lcaNode];
            var totalDistance = distanceNode1 + distanceNode2;

            result[i++] = BigNumber(totalDistance - 1);
        }

        return result;
    }
}

class Program
{
    // NOTE: Time Limit Exceeded 585 / 589 testcases passed

    private static void Main()
    {
        Console.WriteLine("3559. Number of Ways to Assign Edge Weights II");

        Solution solution = new();

        int[][] edges = [[1,2],[1,3],[3,4],[3,5]];
        int[][] queries = [[1,4],[3,4],[2,5]];

        foreach (int num in solution.AssignEdgeWeights(edges, queries))
        {
            Console.WriteLine(num);
        }
    }
}