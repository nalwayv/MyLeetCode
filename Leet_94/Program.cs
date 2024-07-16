public class TreeNode
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

/// <summary>
/// Leet 94 Binary Tree Inorder Traversal
/// </summary>
public class Solution
{
    public void InOrder(TreeNode? root, IList<int> result)
    {
        if (root == null)
        {
            return;
        }

        InOrder(root.left, result);

        result.Add(root.val);

        InOrder(root.right, result);
    }

    public IList<int> InorderTraversal(TreeNode root)
    {
        IList<int> result = [];
        InOrder(root, result);
        return result;
    }
}

internal class Program
{
    private static void Main(string[] args)
    {
        TreeNode n1 = new(1);
        TreeNode n2 = new(2);
        TreeNode n3 = new(3);

        n1.right = n2;
        n2.left = n3;

        Solution sol = new();
        IList<int> result = sol.InorderTraversal(n1);
        foreach (int num in result)
        {
            Console.WriteLine(num);
        }
    }
}