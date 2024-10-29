namespace Leet_117;

internal abstract class Program
{
    private static void PrintConnections(Node? root, string msg)
    {
        if (root == null)
        {
            return;
        }
        
        Node? current = root;
        Console.Write($"{msg} [");
        while (current != null)
        {
            Console.Write($" {current.Value} ");
            current = current.Next;
        }
        Console.WriteLine("]");
    }
    
    private static void Case1(Solution solution)
    {
        Node root = new Node { Value = 1 };
        
        root.Left = new Node { Value = 2 };
        root.Right = new Node { Value = 3 };
        
        root.Left.Left = new Node { Value = 4 };
        root.Left.Right = new Node { Value = 5 };
        root.Right.Right = new Node { Value = 7 };
        
        solution.Connect(root);
        
        PrintConnections(root.Left, "Case 1 level 2:");
        PrintConnections(root.Left.Left, "Case 1 level 3:");
    }
    
    static void Main()
    {
        Console.WriteLine("117. Populating Next Right Pointers in Each Node II");
        
        Solution solution = new();
        
        Case1(solution);
    }
}