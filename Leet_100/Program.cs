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

public class Solution
{
    private void PrintTreeR(TreeNode? node)
    {
        if (node == null)
        {
            return;
        }

        Console.Write($" {node.val} ");
        PrintTreeR(node.left);
        PrintTreeR(node.right);
    }

    public void PrintTree(TreeNode? node)
    {
        Console.Write("[");
        PrintTreeR(node);
        Console.WriteLine("]");
    }

    public bool IsSameTree(TreeNode? p, TreeNode? q)
    {
        if (p == null && q == null)
        {
            return true;
        }

        if (p == null || q == null)
        {
            return false;
        }

        if (p.val != q.val)
        {
            return false;
        }

        return IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
    }
}

internal class Program
{
    private static TreeNode? Build(int[] arr, int i = 0)
    {
        TreeNode? root = null;
        
        if (i < arr.Length && arr[i] != int.MaxValue)
        {
            root = new(arr[i])
            {
                left = Build(arr, 2 * i + 1),
                right = Build(arr, 2 * i + 2)
            };
        }
        return root;
    }

    private static void Check1(Solution sol)
    {        
        TreeNode? tree1 = Build([1,2,3]);
        TreeNode? tree2 = Build([1,2,3]);

        bool check = sol.IsSameTree(tree1, tree2);
        Console.WriteLine($"TreeA = TreeB ? {check}");
    }

    private static void Check2(Solution sol)
    {
        TreeNode? tree1 = Build([1,2]);
        TreeNode? tree2 = Build([1,int.MaxValue,2]);

        bool check = sol.IsSameTree(tree1, tree2);
        Console.WriteLine($"TreeA = TreeB ? {check}");
    }

    private static void Check3(Solution sol)
    {

        TreeNode? tree1 = Build([1,2,1]);
        TreeNode? tree2 = Build([1,1,2]);

        bool check = sol.IsSameTree(tree1, tree2);
        Console.WriteLine($"TreeA = TreeB ? {check}");
    }

    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 100. Same Tree");

        Solution solution = new();
        Check1(solution);
        Check2(solution);
        Check3(solution);
    }
}