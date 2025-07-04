public class Node
{
    public int val;
    public Node? left;
    public Node? right;

    public Node(int val = 0, Node? left = null, Node? right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    public Node? SearchBST(Node? root, int val)
    {
        if(root == null)
        {
            return root;
        }

        if(root?.val == val)
        {
            return root;
        }

        Node? left = SearchBST(root?.left, val);
        if(left != null && left.val ==val){
            return left;
        } 
        
        Node? right = SearchBST(root?.right, val);
        if(right != null && right.val ==val) {
            return right;
        }

        return null;
    }

    public void printTree(Node? root)
    {
        if (root == null)
        {
            return;
        }

        Console.WriteLine($"Node( {root.val} )");
        printTree(root.left);
        printTree(root.right);
    }
}

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 700");


        Node a = new(18);
        Node b = new(2);
        Node c = new(22);
        Node d = new(63);
        Node e = new(84);

        a.left = b;
        a.right = c;
        c.right = d;
        d.right = e;


        Solution solution = new();

        Node? result = solution.SearchBST(a, 2);
        if(result != null)
        {
            solution.printTree(result);
        }
        else
        {
            Console.WriteLine("null");
        }
    }
}