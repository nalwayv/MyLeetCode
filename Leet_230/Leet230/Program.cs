namespace Leet230;

 public class TreeNode {
     public int Val;
     public TreeNode? Left;
     public TreeNode? Right;
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
    private static void Case1(Solution solution)
    {
        var root = new TreeNode { Val = 3 };
        root.Left = new TreeNode { Val = 1 };
        root.Right = new TreeNode { Val = 4 };
        root.Left.Right = new TreeNode { Val = 2 };
        
        int result = solution.KthSmallest(root, 1);
        
        Console.WriteLine($"Case1: [3,1,4,null,2] Kth(1) == 1 ? {result == 1}");
    }
    
    private static void Main()
    {
        Console.WriteLine("Kth Smallest Element in a BST");
        
        var solution = new Solution();
        Case1(solution);
    }
}