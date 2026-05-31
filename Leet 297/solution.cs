using System.Text;

public class TreeNode(int x)
{
    public int val = x;
    public TreeNode? left = null;
    public TreeNode? right = null;
}

public class Codec
{
    // Encodes a tree to a single string.
    public static string Serialize(TreeNode root)
    {
        if (root == null)
            return "";

        Queue<TreeNode> que = new();
        que.Enqueue(root);

        StringBuilder sb = new();
        sb.Append(root.val);

        while (que.Count > 0)
        {
            int count = que.Count;

            for (int i = 0; i < count; i++)
            {
                var current = que.Dequeue();

                sb.Append(',');
                if (current.left != null)
                {
                    que.Enqueue(current.left);
                    sb.Append(current.left.val);
                }
                else
                    sb.Append("null");

                sb.Append(',');
                if (current.right != null)
                {
                    que.Enqueue(current.right);
                    sb.Append(current.right.val);
                }
                else
                    sb.Append("null");
            }
        }

        // Remove trailing nulls and commas
        string result = sb.ToString();
        while (result.EndsWith(",null"))
            result = result.Substring(0, result.Length - 5);

        return result;
    }

    private static bool TryGetValue(string[] values, int idx, out int result)
    {
        result = 0;
        if(idx >= values.Length || values[idx] == "null")
            return false;
        return int.TryParse(values[idx], out result);
    }

    // Decodes your encoded data to tree.
    public static TreeNode Deserialize(string data)
    {
        if (string.IsNullOrEmpty(data))
            return null;

        string[] values = data.Split(',');
        int idx = 0;

        if (!TryGetValue(values, idx++, out int rootVal))
            return null;

        TreeNode root = new(rootVal);
        Queue<TreeNode> que = new();
        que.Enqueue(root);

        while (que.Count > 0 && idx < values.Length)
        {
            var current = que.Dequeue();


            if (TryGetValue(values, idx++, out int leftVal))
            {
                current.left = new(leftVal);
                que.Enqueue(current.left);
            }

            if (TryGetValue(values, idx++, out int rightVal))
            {
                current.right = new(rightVal);
                que.Enqueue(current.right);
            }
        }

        return root;
    }
}


class Program
{
    // helper to create a simple tree
    private static TreeNode Root()
    {
        TreeNode root = new(1);
        root.left = new(2);
        root.right = new(3);
        root.right.left = new(4);
        root.right.right = new(5);
        return root;
    }

    private static void PrintTree(TreeNode root)
    {
        if(root == null) return;

        Stack<TreeNode> stk = new();
        stk.Push(root);

        while (stk.Count > 0)
        {
            var current = stk.Pop();
            
            if (current == null)
                continue;

            Console.WriteLine(current.val);

            stk.Push(current.left);
            stk.Push(current.right);
        }
    }

    private static void Main()
    {
        Console.WriteLine("297. Serialize and Deserialize Binary Tree");
        
        var serialize = Codec.Serialize(Root());
        Console.WriteLine(serialize);

        var root = Codec.Deserialize(serialize);
        PrintTree(root);
    }
}