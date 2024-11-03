namespace Leet_117;

internal abstract class Program
{
    private static void PrintConnections(Node? root, string msg)
    {
        if (root == null)
        {
            return;
        }
        
        Console.Write($"{msg} [");
        for (var current = root; current != null; current = current.Next)
        {
            Console.Write($" {current.Value} ");
        }
        Console.WriteLine("]");
    }
    
    private static void Case1(Solution solution)
    {
        var root = new Node { Value = 1 };
        
        root.Left = new Node { Value = 2 };
        root.Right = new Node { Value = 3 };
        
        root.Left.Left = new Node { Value = 4 };
        root.Left.Right = new Node { Value = 5 };
        root.Right.Right = new Node { Value = 7 };
        
        solution.Connect(root);
        
        PrintConnections(root.Left, "Case 1 level 2:");
        PrintConnections(root.Left.Left, "Case 1 level 3:");
    }

    private static void Main()
    {
        Console.WriteLine("117. Populating Next Right Pointers in Each Node II");
        
        Solution solution = new();
        
        Case1(solution);
    }
}