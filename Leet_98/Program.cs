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
    private void GetValues(TreeNode? root, IList<int> values)
    {
        if (root == null)
        {
            return;
        }

        GetValues(root.left, values);
        values.Add(root.val);
        GetValues(root.right, values);
    }

    public bool IsValidBST(TreeNode? root)
    {
        if (root == null)
        {
            return true;
        }

        List<int> values = [];
        GetValues(root, values);

        if (values.Count == 1)
        {
            return true;
        }
        else
        {
            for (int i = 1; i < values.Count; i++)
            {
                if (values[i - 1] >= values[i])
                {
                    return false;
                }
            }
        }

        return true;
    }
}

internal class Program
{
    private static void Case1(Solution sol)
    {
        TreeNode a = new(2);
        TreeNode b = new(1);
        TreeNode c = new(3);

        a.left = b;
        a.right = c;

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 1 {0}", isValid ? "pass" : "fail");
    }

    private static void Case2(Solution sol)
    {
        TreeNode a = new(5);
        TreeNode b = new(1);
        TreeNode c = new(4);
        TreeNode d = new(3);
        TreeNode e = new(6);

        a.left = b;
        a.right = c;
        c.left = d;
        c.right = e;

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 2 {0}", !isValid ? "pass" : "fail");
    }

    private static void Case3(Solution sol)
    {
        TreeNode a = new(2);
        TreeNode b = new(2);
        TreeNode c = new(2);

        a.left = b;
        a.right = c;

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 3 {0}", !isValid ? "pass" : "fail");

    }

    private static void Case4(Solution sol)
    {
        TreeNode a = new(5);
        TreeNode b = new(4);
        TreeNode c = new(6);
        TreeNode d = new(3);
        TreeNode e = new(7);

        a.left = b;
        a.right = c;
        c.left = d;
        c.right = e;

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 4 {0}", !isValid ? "pass" : "fail");

    }

    private static void Case5(Solution sol)
    {
        TreeNode a = new(1);
        TreeNode b = new(1);

        a.left = b;

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 5 {0}", !isValid ? "pass" : "fail");
    }

    private static void Case6(Solution sol)
    {
        TreeNode a = new(int.MaxValue);

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 6 {0}", isValid ? "pass" : "fail");
    }

    private static void Case7(Solution sol)
    {
        TreeNode a = new(int.MinValue);
        TreeNode b = new(int.MinValue);
        a.left = b;

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 7 {0}", !isValid ? "pass" : "fail");
    }

    private static void Case8(Solution sol)
    {
        TreeNode a = new(int.MinValue);
        TreeNode b = new(int.MaxValue);
        a.right = b;

        bool isValid = sol.IsValidBST(a);
        Console.WriteLine("Case 8 {0}", isValid ? "pass" : "fail");
    }

    private static void Main(string[] args)
    {
        Console.WriteLine("98. Validate Binary Search Tree");

        Solution sol = new();

        Case1(sol);
        Case2(sol);
        Case3(sol);
        Case4(sol);
        Case5(sol);
        Case6(sol);
        Case7(sol);
        Case8(sol);
    }
}