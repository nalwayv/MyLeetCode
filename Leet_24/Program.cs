
public class Node
{
    public int val;
    public Node? next;

    public Node(int val = 0, Node? next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public void PrintNodes(Node? head)
    {
        if(head == null)
        {
            return;
        }

        Node? current = head;
        while (current != null)
        {
            Console.WriteLine(current.val);
            current = current.next;
        }
    }

    public Node? SwapPairs(Node? head)
    {
        Node? curr = head;
        if (curr != null && curr.next != null)
        {
            int tmp = curr.val;
            curr.val = curr.next.val;
            curr.next.val = tmp;

            _ = SwapPairs(curr.next.next);
        }
        return head;
    }
}

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Swap Pairs");

        Solution solution = new();

        Node? a = new(1);
        Node? b = new(2);
        Node? c = new(3);
        Node? d = new(4);

        a.next = b;
        b.next = c;
        c.next = d;
        
        Node ?e = solution.SwapPairs(a); 
        solution.PrintNodes(e);
    }
}