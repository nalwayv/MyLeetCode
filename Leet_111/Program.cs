﻿public class TreeNode
{
    public int val;
    public TreeNode? left;
    public TreeNode? right;
    public TreeNode(int val = 0, TreeNode? left = null, TreeNode? right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    private struct Node
    {
        public TreeNode? Root;
        public int Depth;
    }

    public int MinDepth(TreeNode? root)
    {
        Queue<Node> que = new();
        que.Enqueue(new Node { Root = root, Depth = 1 });

        while (que.Count > 0)
        {
            for (int i = 0; i < que.Count; i++)
            {
                Node curr = que.Dequeue();
                TreeNode? node = curr.Root;
                int depth = curr.Depth;

                if (node == null)
                {
                    continue;
                }

                if (node.left == null && node.right == null)
                {
                    return depth;
                }

                if (node.left != null)
                {
                    que.Enqueue(new Node { Root = node.left, Depth = depth + 1 });
                }

                if (node.right != null)
                {
                    que.Enqueue(new Node { Root = node.right, Depth = depth + 1 });
                }
            }

        }

        return -1;
    }
}

internal class Program
{
    private static void RootA(Solution sol)
    {
        TreeNode a = new(3);
        TreeNode b = new(9);
        TreeNode c = new(20);
        TreeNode d = new(15);
        TreeNode e = new(7);

        a.left = b;
        a.right = c;
        c.left = d;
        c.right = e;

        int resultA = sol.MinDepth(a);
        Console.WriteLine($"Depth= {resultA}");
    }

    private static void RootB(Solution sol)
    {
        TreeNode a = new(2);
        TreeNode b = new(3);
        TreeNode c = new(4);
        TreeNode d = new(5);
        TreeNode e = new(6);

        a.left = b;
        b.left = c;
        c.left = d;
        d.left = e;

        int resultB = sol.MinDepth(a);
        Console.WriteLine($"Depth= {resultB}");
    }

    private static void Main(string[] args)
    {
        Console.WriteLine("111. Minimum Depth of Binary Tree");
        Solution solution = new();

        RootA(solution);
        RootB(solution);
    }
}