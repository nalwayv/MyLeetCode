Console.WriteLine("2265. Count Nodes Equal to Average of Subtree");

var root = new TreeNode(4);
root.left = new TreeNode(8);
root.right = new TreeNode(5);
root.left.left = new TreeNode(0);
root.left.right = new TreeNode(1);
root.right = new TreeNode(5);
root.right.right = new TreeNode(6);

int total = Solution.AverageOfSubtree(root);

Console.WriteLine($"Total subtree's that have an average same as root are {total}");

//---

class TreeNode
{
    public int val;
    public TreeNode? left;
    public TreeNode? right;

    public TreeNode(int val = 0)
    {
        this.val = val;
        left = null;
        right = null;
    }
}

class Solution
{
    struct Result
    { 
        public int sum; 
        public int count; 
    }

    private static Result GetResultForAverageOfSubtree(TreeNode? root, ref int total)
    {
        if (root == null)
        {
            return new Result() { sum = 0, count = 0 };
        }

        var leftResult = GetResultForAverageOfSubtree(root.left, ref total);
        var rightResult = GetResultForAverageOfSubtree(root.right, ref total);

        var sum = leftResult.sum + rightResult.sum + root.val;
        var count = leftResult.count + rightResult.count + 1;
        var average = sum / count;

        if (root.val == average)
        {
            total++;
        }

        return new Result() { sum = sum, count = count };
    }

    public static int AverageOfSubtree(TreeNode root)
    {
        int total = 0;
        _ = GetResultForAverageOfSubtree(root, ref total);
        return total;
    }
}