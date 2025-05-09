namespace Leet449;

public class TreeNode
{
    public int Val;
    public TreeNode? Left;
    public TreeNode? Right;

    public TreeNode(int val)
    {
        Val = val;
        Left = null;
        Right = null;
    }
}

public class Codec
{
    private void CollectValues(TreeNode? root, List<int> values)
    {
        if (root == null)
        {
            return;
        }

        values.Add(root.Val);

        CollectValues(root.Left, values);
        CollectValues(root.Right, values);
    }

    /// Serializes a binary search tree (BST) into a comma-separated string representation
    /// of its node values in pre-order traversal.
    public string Serialize(TreeNode? root)
    {
        if (root == null)
        {
            return string.Empty;
        }
        List<int> values = new();
        CollectValues(root, values);
        return string.Join(',', values);
    }

    private TreeNode InsertTreeNode(TreeNode? root, int val)
    {
        if (root == null)
        {
            root = new TreeNode(val);
        }
        else if (val < root.Val)
        {
            root.Left = InsertTreeNode(root.Left, val);
        }
        else
        {
            root.Right = InsertTreeNode(root.Right, val);
        }
        return root;
    }

    /// Deserializes a serialized binary search tree (BST) given as a comma-separated string
    /// representation of its node values into a TreeNode structure.
    public TreeNode? Deserialize(string data)
    {
        if (string.IsNullOrEmpty(data))
        {
            return null;
        }

        string[] vals = data.Split(',');

        TreeNode? root = null;
        foreach (var val in vals)
        {
            root = InsertTreeNode(root, int.Parse(val));
        }
        return root;
    }
}

static class Helper
{
    private static void PrintValues(TreeNode? root)
    {
        if (root == null)
        {
            return;
        }

        Console.Write($" {root.Val} ");
        PrintValues(root.Left);
        PrintValues(root.Right);
    }

    public static void PrintTree(TreeNode? root)
    {
        if (root == null)
        {
            return;
        }

        Console.Write('[');
        PrintValues(root);
        Console.WriteLine(']');
    }
}

static class Program
{
    static void Main()
    {
        Console.WriteLine("449. Serialize and Deserialize BST");

        TreeNode root = new(2);
        root.Left = new(1);
        root.Right = new(3);

        Codec codec = new();
        string serializedString = codec.Serialize(root);
        Console.WriteLine(serializedString);

        TreeNode? deserializedString = codec.Deserialize(serializedString);
        Helper.PrintTree(deserializedString);
    }
}