namespace Leet133;

public class Node {
    public int val;
    public List<Node> neighbors;

    public Node(int _val) {
        val = _val;
        neighbors = [];
    }
}

internal class Program
{
    public static Node? CopyGraph(Node? node)
    {
        if(node == null)
        {
            return null;
        }

        Dictionary<Node, Node> map = [];
        Stack<Node> stk = new();

        stk.Push(node);
        map.Add(node, new(node.val));

        while (stk.Count != 0)
        {
            Node current = stk.Pop();

            if(current == null) {
                continue;
            }

            foreach (Node neighbor in current.neighbors)
            {
                if(neighbor == null) {
                    continue;
                }

                if(!map.ContainsKey(neighbor))
                {
                    map.Add(neighbor, new(neighbor.val));
                    stk.Push(neighbor);
                }

                map[current].neighbors.Add(map[neighbor]);
            }
        }

        return map[node];
    }

    public static Node? Clone(Node? node, Dictionary<Node, Node> map) {
        if(node == null) 
        {
            return null;
        }

        if(map.TryGetValue(node, out Node? value))
        {
            return value;    
        }

        map.Add(node, new(node.val));

        foreach(Node nei in node.neighbors)
        {
            var clone = Clone(nei, map);
            if (clone == null) {
                continue;
            }

            map[node].neighbors.Add(clone);
        }

        return map[node];
    }

    public static Node? CopyGraph2(Node? node)
    {
        // using recursive stack
        if(node == null)
        {
            return null;
        } 
        Dictionary<Node, Node> map = [];
        return Clone(node, map);

    }

    public static void PrintGraph(Node? node)
    {
        if(node == null)
        {
            return;
        }

        Stack<Node> stk = new();
        HashSet<Node> vis = [];

        stk.Push(node);

        while (stk.Count != 0)
        {
            Node current = stk.Pop();
            if (vis.Contains(current))
            {
                continue;
            }

            vis.Add(current);

            Console.Write($"Node({current.val}) [");
            foreach (Node nei in current.neighbors)
            {
                Console.Write($" {nei.val} ");
                stk.Push(nei);
            }
            Console.WriteLine("]");
        }
    }

    private static void Main()
    {
        Console.WriteLine("Leet 133!");

        Node a = new(1);
        Node b = new(2);
        Node c = new(3);
        Node d = new(4);

        a.neighbors.Add(b);
        a.neighbors.Add(d);

        b.neighbors.Add(a);
        b.neighbors.Add(c);

        c.neighbors.Add(b);
        c.neighbors.Add(d);

        d.neighbors.Add(a);
        d.neighbors.Add(c);

        PrintGraph(a);
        PrintGraph(CopyGraph2(a));
    }
}