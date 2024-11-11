namespace Leet230;

 public class TreeNode {
     public int Val;
     public TreeNode? Left;
     public TreeNode? Right;
     
     public TreeNode(int val=0, TreeNode? left=null, TreeNode? right=null) 
     {
        this.Val = val;
        this.Left = left;
        this.Right = right;
     }
 }

 public class Solution {
     private static TreeNode? Kth(TreeNode? root, int k, ref int count) 
     {
         if (root == null)
         {
             return null;
         }

         TreeNode? left = Kth(root.Left, k, ref count);
         if (left != null)
         {
             return left;
         }

         return ++count == k ? root : Kth(root.Right, k, ref count);
     }

     public int KthSmallest(TreeNode root, int k) 
     {
         int count = 0;
         TreeNode? kth = Kth(root, k, ref count);

         if (kth != null)
         {
             return kth.Val;
         }
         
         return -1;
     }
 }

internal static class Program
{
    private static void Main()
    {
        Console.WriteLine("Kth Smallest Element in a BST");
        
        var root = new TreeNode(3);
        root.Left = new TreeNode(1);
        root.Right = new TreeNode(4);
        root.Left.Right = new TreeNode(2);
        
        var solution = new Solution();
        Console.WriteLine($"[3,1,4,null,2] Kth(1) == {solution.KthSmallest(root, 1)}");
    }
}