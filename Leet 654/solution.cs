namespace Leet654;

public class TreeNode
{
    public int Value;
    public TreeNode? Left;
    public TreeNode? Right;

    public TreeNode(int value, TreeNode? left=null, TreeNode? right=null)
    {
        Value = value;
        Left = left;
        Right = right;
    }
}

public class Solution 
{
    /// <summary>
    /// Constructs the maximum binary tree from the given array of integers.
    /// </summary>
    public TreeNode? ConstructMaximumBinaryTree(int[] nums) 
    {
        if (nums.Length == 0)
        {
            return null;
        }

        int idx = 0;
        int max = nums[0];
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] > max)
            {
                max = nums[i];
                idx = i;
            }
        }

        var root = new TreeNode(max);
        root.left = ConstructMaximumBinaryTree(nums[..idx]);
        root.right = ConstructMaximumBinaryTree(nums[(idx + 1)..]);

        return root;
    }
}

class Program
{
    private static void PrintTree(TreeNode? root)
    {
        while (true)
        {
            if (root == null)
            {
                return;
            }
            
            PrintTree(root.Left);
            Console.Write($" {root.Value} ");
            root = root.Right;
        }
    }

    static void Main()
    {
        Console.WriteLine("654. Maximum Binary Tree");
        var solution = new Solution();
        TreeNode? root = solution.ConstructMaximumBinaryTree([ 3, 2, 1, 6, 0, 5 ]);
        PrintTree(root);
    }
}