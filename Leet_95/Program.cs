namespace Leet95;

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
    private void PrintT(Node? root)
    {
        if (root == null)
        {
            Console.Write(" (null) ");
            return;
        }

        Console.Write($" ({root.val}) ");
        PrintT(root.left);
        PrintT(root.right);
    }

    public void PrintTree(Node? root)
    {
        Console.Write("[");
        PrintT(root);
        Console.WriteLine("]");
    }

    private IList<Node?> Generate(int end, int start=1)
    {
        IList<Node?> nodes = [];
        if (start > end)
        {
            nodes.Add(null);
        }
        else
        {
            for (int i = start; i <= end; i++)
            {
                IList<Node?> leftNodes = Generate(i - 1, start);
                IList<Node?> rightNodes = Generate(end, i + 1);

                foreach (Node ?left in leftNodes)
                {
                    foreach (Node ?right in rightNodes)
                    {
                        Node newNode = new(i)
                        {
                            left = left,
                            right = right
                        };

                        nodes.Add(newNode);
                    }
                }
            }
        }

        return nodes;
    }

    public IList<Node?> GenerateTrees(int n)
    {
        return Generate(n);
    }
}

internal class Program
{

    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 95 Unique Binary Search Trees II");

        Solution solution = new();



        int cat = solution.CatalanNumber(3);
        System.Console.WriteLine(cat);


        IList<Node?> result = solution.GenerateTrees(3);
        foreach (Node ?root in result)
        {
            solution.PrintTree(root);
        }

    }
}