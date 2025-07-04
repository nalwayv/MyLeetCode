using System.IO.Compression;
using System.Runtime.CompilerServices;

public class Node
{
    public int val;
    public Node? left;
    public Node? right;

    public Node(int val = 0, Node? left = null, Node? right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    private int GetMaxDepth(Node? root, int depth = 0)
    {
        if(root == null)
        {
            return depth;
        }

        int left = GetMaxDepth(root.left, depth + 1);
        int right = GetMaxDepth(root.right, depth + 1);
        
        return int.Max(left, right);
    }

    public int MaxDepth(Node? root)
    {
        return GetMaxDepth(root);
    }
}

internal class Program
{
    private static void Test1(Solution solution)
    {
        Node a = new(3);
        Node b = new(9);
        Node c = new(20);
        Node d = new(15);
        Node e = new(7);

        a.left = b;
        a.right = c;
        c.left = d;
        c.right = e;

        int depth = solution.MaxDepth(a);
        Console.WriteLine($"Test1 Expect 3 Output = {depth}");
    }

    private static void Test2(Solution solution)
    {
        Node a = new(1);
        Node b = new(2);

        a.right = b;

        int depth = solution.MaxDepth(a);
        Console.WriteLine($"Test2 Expect 2 Output = {depth}");
    }


    private static void Main()
    {
        Console.WriteLine("Leet 104 Maximun depth of a binary tree");

        Solution solution = new();
        Test1(solution);
        Test2(solution);
    }
}