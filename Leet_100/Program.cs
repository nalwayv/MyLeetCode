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
    public bool IsSameTree(TreeNode? p, TreeNode? q)
    {
        if (p == null && q == null)
        {
            return true;
        }

        if (p != null && q != null && p.val == q.val)
        {
            bool left = IsSameTree(p.left, q.left);
            bool right = IsSameTree(p.right, q.right);

            return left && right;
        }

        return false;
    }
}

internal class Program
{
    private static void Check1(Solution sol)
    {
        TreeNode? a1 = new(1);
        TreeNode? b1 = new(2);
        TreeNode? c1 = new(3);

        a1.left = b1;
        a1.right = c1;

        TreeNode? a2 = new(1);
        TreeNode? b2 = new(2);
        TreeNode? c2 = new(3);

        a2.left = b2;
        a2.right = c2;

        bool check = sol.IsSameTree(a1, a2);

        Console.WriteLine($"[1,2,3] = [1,2,3] ? {check}");
    }

    private static void Check2(Solution sol)
    {
        TreeNode a1 = new(1);
        TreeNode b1 = new(2);

        a1.left = b1;

        TreeNode a2 = new(1);
        TreeNode b2 = new(2);

        a2.right = b2;

        bool check = sol.IsSameTree(a1, a2);

        Console.WriteLine($"[1,2] = [1,null,2] ? {check}");
    }

    private static void Check3(Solution sol)
    {
        TreeNode a1 = new(1);
        TreeNode b1 = new(2);
        TreeNode c1 = new(1);

        a1.left = b1;
        a1.right = c1;

        TreeNode a2 = new(1);
        TreeNode b2 = new(1);
        TreeNode c2 = new(2);

        a2.left = b2;
        a2.right = c2;

        bool check = sol.IsSameTree(a1, a2);

        Console.WriteLine($"[1,2,1] = [1,1,2] ? {check}");
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