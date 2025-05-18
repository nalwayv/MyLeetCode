using Microsoft.VisualBasic;

public class TreeNode
{
    public  int val;
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
    int idx = 0;
    
    private void PrintTreeR(TreeNode? node)
    {
        if (node == null)
        {
            return;
        }

        PrintTreeR(node.left);
        PrintTreeR(node.right);
        Console.Write($" {node.val} ");
    }

    public void PrintTree(TreeNode? node)
    {
        Console.Write("[");
        PrintTreeR(node);
        Console.WriteLine("]");
    }

    private TreeNode? Build(int start, int end, int[] arr, Dictionary<int, int> cache)
    {
        if (start > end || idx < 0)
        {
            return null;
        }

        TreeNode node = new(arr[idx--]);

        if (cache.TryGetValue(node.val, out int at))
        {
            node.left = Build(start, at - 1, arr, cache);
            node.right = Build(at + 1, end, arr, cache);
        }

        return node;
    }

    public TreeNode? BuildTree(int[] inorder, int[] postorder)
    {
        Dictionary<int, int> cache = [];
        for (int i = 0; i < inorder.Length; i++)
        {
            cache[inorder[i]] = i;
        }

        idx = postorder.Length - 1;
        int n = inorder.Length - 1;

        return Build(0, n, postorder, cache);
    }
}


internal class Program
{
    private static void Main(string[] args)
    {
        // Construct Binary Tree from Inorder and Postorder Traversal
        Console.WriteLine("Leet 105");

        Solution solution = new();
        int[] inorder = [9,3,15,20,7];
        int[] postorder = [3,9,20,15,7];

        // [3,9,20,null,null,15,7] CORRECT
        // [9,null,3,15,null,null,20,7] WRONG
        TreeNode? result = solution.BuildTree(inorder, postorder);
        solution.PrintTree(result);
    }
}