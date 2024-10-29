namespace Leet_117;

public class Node
{
    public int Value;
    public Node? Left;
    public Node? Right;
    public Node? Next;
}

public class Solution
{
    public Node? Connect(Node? root)
    {
        if (root == null) return root;

        Queue<Node?> que = new();
        que.Enqueue(root);
        List<Node> nodes = [];

        while (que.Count > 0)
        {
            int count = que.Count;
            
            for (int i = 0; i < count; i++)
            {
                Node? current = que.Dequeue();
                if (current == null) continue;
                
                if (current.Left != null)
                {
                    que.Enqueue(current.Left);
                    nodes.Add(current.Left);
                }

                if (current.Right != null)
                {
                    que.Enqueue(current.Right);
                    nodes.Add(current.Right);
                }
            }

            if (nodes.Count > 1)
            {
                for (int j = 1; j < nodes.Count; j++)
                {
                    nodes[j - 1].Next = nodes[j];
                }
            }
            nodes.Clear();
            
        }
        
        return root;
    }
}